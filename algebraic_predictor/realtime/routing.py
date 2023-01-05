from django.urls import path

from .consumers import WSConsumer

ws_urlpatterns = [
    path('ws/counter/', WSConsumer.as_asgi())
]
