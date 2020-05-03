# -*- coding: utf-8 -*-

from django.test import TestCase, override_settings
from . import views

class SettingsParseTestCase(TestCase):
    '''
    Test if parsing of the settings works as intended and that it overwrites the
    defaults, but keeps them where they are not defined
    '''
    def test_confirm_default_success_message(self):
        '''
        Confirm default success message is not overwritten if not defined in
        application settings
        '''
        test_settings = views.mailchimp_parse_settings()
        self.assertEqual(test_settings['success_message'], views.MAILCHIMP_DEFAULT_MESSAGES['success_message'])

    @override_settings(MAILCHIMP_MESSAGES = { 'success_message': 'Test' })
    def test_overwrite_default_success_message(self):
        '''
        Confirm that we can overwrite default success message from application
        settings. Also do not touch other fields.
        '''
        test_settings = views.mailchimp_parse_settings()
        self.assertEqual(test_settings['success_message'], 'Test')
        self.assertEqual(test_settings['error_member_exists'], views.MAILCHIMP_DEFAULT_MESSAGES['error_member_exists'])

    def test_confirm_default_error_member_exists(self):
        '''
        Confirm default error message when member exists is not overwritten if
        not defined in application settings
        '''
        test_settings = views.mailchimp_parse_settings()
        self.assertEqual(test_settings['error_member_exists'], views.MAILCHIMP_DEFAULT_MESSAGES['error_member_exists'])

    @override_settings(MAILCHIMP_MESSAGES = { 'error_member_exists': 'Test1' })
    def test_overwrite_default_error_member_exists(self):
        '''
        Confirm that we can overwrite default error message when member exists
        from application settings.
        '''
        test_settings = views.mailchimp_parse_settings()
        self.assertEqual(test_settings['error_member_exists'], 'Test1')
        self.assertEqual(test_settings['success_message'], views.MAILCHIMP_DEFAULT_MESSAGES['success_message'])


