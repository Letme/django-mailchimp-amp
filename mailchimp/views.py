import base64
import json
import logging
import os
from django.conf import settings
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import requires_csrf_token
from django.template import RequestContext
from mailchimp3 import MailChimp
from mailchimp3.mailchimpclient import MailChimpError
from requests_toolbelt.multipart import decoder

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def mailchimp_proxy_view(request):
    '''
    We want to bypass the undefined CORS policy on the MailChimp servers, so this is a proxy view which does that
    '''
    if request.method == 'POST':
        mailchimp = MailChimp(mc_api=settings.MAILCHIMP_API, mc_user=settings.MAILCHIMP_USERNAME, timeout=10.0)

        email = request.POST.get('EMAIL')
        try:
            validate_email(email)
        except ValidationError as e:
            error_response = {
                'error': str(e)
            }
            return HttpResponse(json.dumps(error_response), content_type='application/json', status=400)

        try:
            lists = mailchimp.lists.all()
            logger.info(lists)
            members = mailchimp.lists.members.create(settings.MAILCHIMP_LISTID, {
                'email_address': email,
                'status': 'pending',
            })
        except MailChimpError as e:
            print(e)
            error_response = {
                'error': str(e.args[0].get("title"))
            }
            return (HttpResponse(json.dumps(error_response), content_type='application/json', status=400))

        positive_response = {
            'body': ''
        }
        return (JsonResponse(positive_response))
    else:
        return (HttpResponse(status=400))
