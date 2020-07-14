from channels.routing import ProtocolTypeRouter

application = ProtocolTypeRouter({
    # Empty for now (http->django views is added by default)
})

""" from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import chat.routing

application = ProtocolTypeRouter({
    # (http->django views is added by default)
    'websocket': AuthMiddlewareStack(
        URLRouter(
            chat.routing.websocket_urlpatterns
        )
    ),
})

application = [
    # To set up the websocket routing
   include(“chat-app.routing.routing_websocket”, path=r”^/socket/”),
    # For chat join, leave, and send
    include(“chat-app.routing.routing_chat”),
] """

""" from channels.staticfiles import StaticFilesConsumer
from . import consumers """

""" channel_routing = {
    # This makes Django serve static files from settings.STATIC_URL, similar
    # to django.views.static.serve. This isn't ideal (not exactly production
    # quality) but it works for a minimal example.
    'http.request': StaticFilesConsumer(),

    # Wire up websocket channels to our consumers:
    'websocket.connect': consumers.ws_connect,
    'websocket.receive': consumers.ws_receive,
    'websocket.disconnect': consumers.ws_disconnect,
} """