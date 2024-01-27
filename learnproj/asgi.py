
import os
from django.core.asgi import get_asgi_application
from channels.routing import import ProtocolTypeRouter, URLRouter
from websocket.middlewares import WebSocketJWTAuthMiddleware

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'learnproj.settings')
 
application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),
        "websocket": WebSocketJWTAuthMiddleware(URLRouter(learnapp.routing.websocket_urlpatterns)),
    }
)

