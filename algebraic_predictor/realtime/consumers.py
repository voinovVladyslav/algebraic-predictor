import json
import time

from channels.generic.websocket import WebsocketConsumer


class WSConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        number = 0
        while True:
            self.send(json.dumps({'number': number}))
            time.sleep(1)
            number += 1

    def disconnect(self, code):
        return super().disconnect(code)
