import time
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from rest_framework.authtoken.models import Token

from backend.celery import app


channel_layer = get_channel_layer()


@app.task
def send_log(source, token):
    words = source.split()
    for word in words:
        time.sleep(1)
        async_to_sync(channel_layer.group_send)(
            token,
            {
                'type': 'send_log_record',
                'log': word,
            }
        )
