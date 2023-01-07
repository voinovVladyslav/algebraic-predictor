from random import randint
from backend.celery import app
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync


channel_layer = get_channel_layer()


@app.task
def get_random_number():
    n = randint(0, 100_000_000)
    async_to_sync(channel_layer.group_send)(
        'randint',
        {
            'type': 'send_randint',
            'text': n,
        }
    )
