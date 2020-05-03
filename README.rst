.. image:: https://img.shields.io/badge/License-GPL%20v3-blue.svg
    :target: https://www.gnu.org/licenses/gpl-3.0
    :alt: GPL3 License

.. image:: https://badge.fury.io/py/django-mailchimp-amp.svg
    :target: https://badge.fury.io/py/django-mailchimp-amp
    :alt: Pypi packaged release

.. image:: https://travis-ci.org/letme/django-mailchimp-amp.svg?branch=master
    :target: https://travis-ci.org/letme/django-mailchimp-amp
    :alt: Build status

.. image:: https://img.shields.io/badge/Documentation-published-brightgreen.svg
    :target: https://letme.github.io/django-mailchimp-amp/
    :alt: Documentation

.. image:: https://codecov.io/gh/letme/django-mailchimp-amp/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/letme/django-mailchimp-amp
    :alt: Code Coverage

.. image:: https://codeclimate.com/github/letme/django-mailchimp-amp/badges/gpa.svg
    :target: https://codeclimate.com/github/letme/django-mailchimp-amp
    :alt: Code Climate Status

.. image:: https://codeclimate.com/github/letme/django-mailchimp-amp/badges/issue_count.svg
    :target: https://codeclimate.com/github/letme/django-mailchimp-amp
    :alt: Issue Count

.. image:: https://requires.io/github/letme/django-mailchimp-amp/requirements.svg?branch=master
    :target: https://requires.io/github/letme/django-mailchimp-amp/requirements/?branch=master
    :alt: Requirements Status

.. image:: https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat
    :target: https://github.com/letme/django-mailchimp-amp/issues
    :alt: Contributions welcome

===============================================
Django Mailchimp AMP embedded subscription form
===============================================

Django app for easy embedding of the Mailchimp subscription form to AMP pages.

Quick start
===========

#. Install ``django-mailchimp-amp``:

    .. code-block:: bash

        pip install django-mailchimp-amp

    or from sources

    .. code-block:: bash

        pip install git+https://github.com/letme/django-mailchimp-amp

#. Add ``django-mailchimp-amp`` to ``INSTALLED_APPS`` in your Django ``settings.py``. Also make sure you add your
   MailChimp api key, username and listids

    .. code-block:: python

        INSTALLED_APPS = [
               ...
               'django-mailchimp-amp',
           ]
        MAILCHIMP_API = 'yourmailchimpapikey'
        MAILCHIMP_USERNAME = 'yourmailchimp@mail'
        MAILCHIMP_LISTID = 'mailchimplistid'


#. Add ``django-mailchimp-amp`` to ``urlpatterns`` in your project ``urls.py``:

    .. code-block:: python

        urlpatterns = [
            ...
            path('mailchimp/', include('django-mailchimp-amp.urls')),
        ]

#. Add template tags to your templates where you want subscription form to be presented:

    .. code-block:: html+django

        <head>
            <!-- if you did not include amp-form and amp-mustache for anything else -->
            {% include "django-mailchimp-amp/scripts_form.html" %}

            <style amp-custom>
            /* Include default form style template */
			{% include "django-mailchimp-amp/style_form.css" %}
            </style>
        </head>
        <body>
            <!-- Include the subscription form where pre_subscribe_text appears above/before the subscription form -->
    		{% include "django-mailchimp-amp/subscribe_form.html" with mailchimp_pre_subscribe_text="If you want to receive our awesome stuff you can subscribe to our newsletter:" %}
        </body>


Contributing
============

Any contribution is welcome as well as reporting issues/bugs or requesting features. Do not be shy and open a pull
request and I will do my best to help you include your contribution into the repository. Keep in mind that reporting a
bug or requesting a feature is also considered as contribution, even if you do not have development skills to implement
it.

Development setup
=================

To run tests and checks we use tox.

.. code-block:: bash

    # to install tox
    pip3 install tox

    # to run tests
    tox

