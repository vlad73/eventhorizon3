import logging
from google.appengine.api import xmpp
from google.appengine.api.mail_errors import InvalidEmailError
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from google.appengine.api.mail import send_mail

@csrf_exempt
def send_notification_message(request):
    if request.POST:
        # perform GET
        protocol = request.GET.get("protocol","email")
        if protocol == "email":
            try:
                send_email_message(request)
                return HttpResponse("message was sent successfully!")
            except InvalidEmailError:
                return HttpResponse("wrong email address")


            #send_xmpp_message(request)

def send_email_message(request):
     # normalize the given amount
    sender = request.POST.get("sender")
    to = request.POST.get("to")
    subject = request.POST.get("subject")
    body  = request.POST.get("body")
    logging.info('mail from %s to %s body %s' % (sender,to, body))
    send_mail(sender, to, subject, body)

def send_xmpp_message(request):
    to = request.POST.get("to")
    sender = request.POST.get("sender")
    msg  = request.Post.get("body")
    chat_message_sent = False

    if xmpp.get_presence(to):
        status_code = xmpp.send_message(to, msg, sender)
        chat_message_sent = (status_code != xmpp.NO_ERROR)

    if not chat_message_sent:
        # Send an email message instead...
        return HttpResponse("message error!")
    else:
        return HttpResponse("message was sent successfully!")




