from django.urls import path

from . import consumers

ws_urlpatterns = [
    path('ws/console/', consumers.ConsoleConsumer.as_asgi()),
]
