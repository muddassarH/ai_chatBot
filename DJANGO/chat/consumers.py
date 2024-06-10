import json
from channels.generic.websocket import AsyncWebsocketConsumer
from groq import AsyncGroq
from django.conf import settings
import asyncio
import sys

api_key = settings.APIKEY
client = AsyncGroq(api_key=api_key)

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = f"chat_{self.room_name}"
        self.conversation_history = []
        # Join room group
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        
        if message.lower() in {"exit", "quit"}:
            await self.send(text_data=json.dumps({"message": "Ending Chat Session"}))
            return
        self.conversation_history.append({"role": "user", "content": message})
        response_data = await self.send_code_to_api()
        await self.send(text_data=json.dumps({"message": response_data}))

    async def send_code_to_api(self):
        response = ""
        stream = await client.chat.completions.create(
            messages=[
            {
                "role": "system",
                "content": "you are a helpful assistant"
            }] + self.conversation_history,
            model="llama3-8b-8192",
            temperature=0.5,
            max_tokens=8024,
            top_p=1,
            stop=None,
            stream=True,
        )
        async for chunk in stream:
            if chunk.choices[0].delta.content is not None:
                response += chunk.choices[0].delta.content
        if not response:
            response = "I'm sorry, I couldn't understand your message."

        return response