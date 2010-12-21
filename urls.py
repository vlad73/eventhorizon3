from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^_ah/xmpp/message/chat/', 'gateway.services.on_message'),
    (r'^push_msg/', 'gateway.services.push_message'),
    ('^$', 'django.views.generic.simple.direct_to_template',
     {'template': 'home.html'}),
)
