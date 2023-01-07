from django.urls import path

from .consumers import RandintConsumer, ConsoleConsumer

ws_urlpatterns = [
    path('ws/randint/', RandintConsumer.as_asgi()),
    path('ws/console/', ConsoleConsumer.as_asgi()),
]
