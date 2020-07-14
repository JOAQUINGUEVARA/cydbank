#from django.conf.urls import include, url
from django.urls import path,include,re_path
from chat.views import about,index,room

chat_patterns = ([
    path('',index, name='index'),
    path('<str:room_name>/', room, name='room'),
    #path('', about, name='about'),
    #path('', new_room, name='new_room'),
    #path('(P<label>)', chat_room, name='chat_room')
    #re_path(r'^(?P<room_name>[^/]+)/$',room,name='room')

], 'chat')

""" from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator, OriginValidator
from chat.consumers import ChatConsumer """

""" application = ProtocolTypeRouter({
# Empty for now (http->django views is added by default)
    'websocket': AllowedHostsOriginValidator(
        AuthMiddlewareStack(
            URLRouter(
                [
                    re_path(r"^messages/(?P<username>[\w.@+-]+)", ChatConsumer),
                ]
            )
        )
    )
}) """

#path('', views.about, name='about'),
#path('', views.new_room, name='new_room'),
#path('(P<label>)', views.chat_room, name='chat_room'),