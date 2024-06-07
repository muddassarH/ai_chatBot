from django.conf import settings
from groq import Groq


api_key = settings.APIKEY
client = Groq(api_key=api_key)


def send_code_to_api(question,system_role):

    res = client.chat.completions.create(
        messages=[
        # Set an optional system message. This sets the behavior of the
        # assistant and can be used to provide specific instructions for
        # how it should behave throughout the conversation.
        {
            "role": "system",
            "content": f"{system_role}"
        },
        # Set a user message for the assistant to respond to.
        {
            "role": "user",
            "content": f"{question}",
        }
    ],
        model="llama3-8b-8192",
    )
    return res.choices[0].message.content
