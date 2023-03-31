from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('chat/<str:user>', consumers.ChatConsumer.as_asgi()),
]
