import os
from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')


app = Celery('backend')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = {
    'get_randint_3s': {
        'task': 'realtime.tasks.get_random_number',
        'schedule': 3.0
    }
}

app.autodiscover_tasks()
