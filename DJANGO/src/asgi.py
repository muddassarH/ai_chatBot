import os, django
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from channels.layers import get_channel_layer



os.environ.setdefault("DJANGO_SETTINGS_MODULE", "src.settings")
django.setup()

django_asgi_app = get_asgi_application()
channel_layer = get_channel_layer()

import chat.routing as route



application = ProtocolTypeRouter({
    "http": django_asgi_app ,
    "https": django_asgi_app ,
    'websocket': AuthMiddlewareStack(
        URLRouter(
            route.websocket_urlpatterns
        )
    ),
})
