#_*_coding: utf-8_*_

import base64
import hashlib
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

# define defaults
MAILCHIMP_DEFAULT_MESSAGES = {
    'success_message': 'Success! Thanks for subscribing to our newsletter! Please check your email to confirm subscription!',
    'error_member_exists': 'You are already member of our mailing list. We resent you the for confirmation email now.',
}

def mailchimp_parse_settings():
    '''
    Set defaults for the settings in case the general settings do not have all defined values or some are missing
    '''
    merged_settings = {}
    # here we go
    for key in MAILCHIMP_DEFAULT_MESSAGES.keys():
        try:
            merged_settings[key] = settings.MAILCHIMP_MESSAGES[key]
        except (KeyError, AttributeError) as e:
            merged_settings[key] = MAILCHIMP_DEFAULT_MESSAGES[key]

    return merged_settings

def mailchimp_proxy_view(request):
    '''
    We want to bypass the undefined CORS policy on the MailChimp servers, so this is a proxy view which does that
    '''
    view_settings = mailchimp_parse_settings()

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
            email_hash = hashlib.md5(email.encode())
            members = mailchimp.lists.members.create(settings.MAILCHIMP_LISTID, {
                'email_address': email,
                'status': 'pending',
            })
            positive_response = {
                'message': view_settings['success_message']
            }
            return (JsonResponse(positive_response))
        except MailChimpError as e:
            print(str(e))
            error_title = str(e.args[0].get("title"))
            if error_title == 'Member Exists':
                members = mailchimp.lists.members.update(settings.MAILCHIMP_LISTID, email_hash.hexdigest(), {
                    'email_address': email,
                    'status': 'pending',
                })
                error_response = {
                    'error': view_settings['error_member_exists']
                }
            elif error_title == 'Forgotten Email Not Subscribed':
                error_response = {
                    'error': str(e.args[0].get("detail"))
                }
            else:
                error_response = {
                    'error': str(e.args[0].get("title"))
                }
            return (HttpResponse(json.dumps(error_response), content_type='application/json', status=400))

    else:
        return (HttpResponse(status=400))
