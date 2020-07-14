""" from channels.staticfiles import StaticFilesConsumer
from . import consumers

channel_routing = {
    # This makes Django serve static files from settings.STATIC_URL, similar
    # to django.views.static.serve. This isn't ideal (not exactly production
    # quality) but it works for a minimal example.
    'http.request': StaticFilesConsumer(),

    # Wire up websocket channels to our consumers:
    'websocket.connect': consumers.ws_connect,
    'websocket.receive': consumers.ws_receive,
    'websocket.disconnect': consumers.ws_disconnect,
} """

f""" rom django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<room_name>\w+)/$', consumers.ChatConsumer),
] """

""" from channels import route
from .consumers import websocket_connect, websocket_receive, websocket _disconnect, join_chat, leave_chat, send_chat
routing_websocket = [
    route(“websocket.connect”, websocket_connect),
    route(“websocket.receive”, websocket_receive),
    route(“websocket.disconnect”, websocket_disconnect),
]
routing_chat = [
    route(“chat.receive”, join_chat, command=”^join$”),
    route(“chat.receive”, leave_chat, command=”^leave$”),
    route(“chat.receive”, send_chat, command=”^send$”),
] """

from channels import route

# This function will display all messages received in the console
def message_handler(message):
    print(message['text'])


channel_routing = [
    route("websocket.receive", message_handler)  # we register our message handler
]