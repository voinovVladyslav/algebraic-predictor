from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from rest_framework.authtoken.models import Token

from backend.celery import app


channel_layer = get_channel_layer()


@app.task
def send_email(token):
    user = Token.objects.get(key=token).user
    async_to_sync(channel_layer.group_send)(
        token,
        {
            'type': 'send_email',
            'text': user.email,
        }
    )
