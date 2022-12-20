from datetime import datetime


def get_now_time() -> str:
    return datetime.now().strftime('%d-%m-%Y')
