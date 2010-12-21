# -*- coding: UTF-8 -*-

from google.appengine.api import xmpp
from gateway.server_protocol import save_or_update_pattern, get_patterns
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

    if action == 'extract_patterns':
        result = extract_patterns(data)
    else:
        result = "could not understand your request"

    message.reply(simplejson.dump(result))