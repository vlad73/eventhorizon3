# -*- coding: UTF-8 -*-

from google.appengine.api import xmpp
from gateway.server_protocol import save_or_update_pattern
from django.views.decorators.csrf import csrf_exempt
import logging
from django.utils import simplejson

#noinspection PyUnresolvedReferences
@csrf_exempt
def on_message(request):
    message = xmpp.Message(request.POST)
    logging.info("Received message: %s" % message.body)
    data = simplejson.loads(message.body)

    action = data['action']

    if action == 'save_pattern':
        result = save_or_update_pattern(data)

    elif action =='get_patterns':
        result = get_patterns(data)
        simplejson.dump(result)

    else:
        result = "could not understand your request"

    message.reply(result)