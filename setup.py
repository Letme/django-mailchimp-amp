#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name="django-mailchimp-amp",
    packages=find_packages(),
    package_data={"mailchimp-amp": ["templates/mailchimp/*.html", "templates/mailchimp/*.css"]},
    use_scm_version=True,
    author="Crt Mori",
    author_email="crt@the-mori.com",
    url="https://github.com/letme/django-mailchimp-amp",
    description="Django app for easy embeding of MailChimp subscription form in AMP page",
    long_description_content_type="text/x-rst",
    long_description=open("README.rst", encoding="utf-8").read(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Environment :: Plugins",
        "Framework :: Django",
        "Framework :: Django :: 3.0",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GPLv3 License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Internet :: WWW/HTTP",
    ],
    keywords=["django", "mailchimp", "amp"],
    install_requires=["mailchimp3>=3.0.13", "Django >= 3.0",],
    setup_requires=["nose", "readme", "setuptools_scm"],
    tests_require=["Django", "requests >= 2.19", "coverage"],
    test_suite="nose.collector",
)
