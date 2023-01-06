from django.urls import path

from .consumers import RandintConsumer

ws_urlpatterns = [
    path('ws/randint/', RandintConsumer.as_asgi())
]
