from channels.generic.websocket import AsyncWebsocketConsumer


class ConsoleConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        user = self.scope['user']
        if not user:
            self.close(code=4004)
            return
        token = self.scope['token']
        await self.channel_layer.group_add(token, self.channel_name)
        self.groups.append(token)
        await self.accept()

    async def send_email(self, event):
        email = event['text']
        await self.send(email)
