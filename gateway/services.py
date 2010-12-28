# -*- coding: UTF-8 -*-

from google.appengine.api import xmpp
from gateway.server_protocol import extract_patterns
from django.views.decorators.csrf import csrf_exempt
import logging
from django.utils import simplejson

#noinspection PyUnresolvedReferences
def handle_message(json):
    logging.info("Received message: %s" % json)
    data = simplejson.loads(json)
    action = data['action']
    if action == 'extract_patterns':
        result = extract_patterns(data)
        result.append({'discussion_id': data['discussion_id']})
    else:
        result = "could not understand your request"
    return simplejson.dumps(result)

@csrf_exempt
def on_message(request):
    message = xmpp.Message(request.POST)
    message.reply(handle_message(message.body))