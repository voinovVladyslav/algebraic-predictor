from channels.generic.websocket import AsyncWebsocketConsumer


class RandintConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add('randint', self.channel_name)
        self.groups.append('randint')
        await self.accept()

    async def send_randint(self, event):
        number = event['text']
        await self.send(str(number))


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

    async def send_randint(self, event):
        number = event['text']
        await self.send(str(number))
