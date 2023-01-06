from channels.generic.websocket import AsyncWebsocketConsumer


class RandintConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add('randint', self.channel_name)
        await self.accept()

    async def disconnect(self, message):
        await self.channel_layer.group_discard('randint', self.channel_name)

    async def send_randint(self, event):
        number = event['text']
        await self.send(str(number))
