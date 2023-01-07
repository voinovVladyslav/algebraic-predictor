from channels.db import database_sync_to_async
from rest_framework.authtoken.models import Token


@database_sync_to_async
def get_user(token):
    try:
        return Token.objects.get(key=token).user
    except Token.DoesNotExist:
        return


class TokenAuthMiddleware:
    def __init__(self, app):
        self.app = app

    async def __call__(self, scope, receive, send):
        try:
            token = scope['subprotocols'][1]
            user = await get_user(token)
            scope['user'] = user
            scope['token'] = token
        except KeyError:
            scope['user'] = None
        return await self.app(scope, receive, send)
