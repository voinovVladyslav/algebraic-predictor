from random import randint
from backend.celery import app


@app.task
def get_random_number():
    n = randint(0, 100_000_000)
    print('number:', n)
    return n
