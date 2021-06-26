#!/bin/env python

import setuptools

with open('README.md', 'r', encoding='utf=8') as fh:
    long_description = fh.read()

setuptools.setup(
        name = 'qxf2-newsletter-automation',
        version = '0.0.1',
        author = 'shivahari.p',
        author_email = 'shivahari@qxf2.com',
        description = 'A Qxf2 Newsletter automation app',
        long_description = long_description,
        long_description_content_type = 'text/markdown',
        url = 'https://github.com/shivahari/newsletter_automation',
        classifiers = [
            'Programming Language :: Python :: 3',
            'License :: OSI :: MIT',
            'Operating System :: OS Independent'],
        package_dir = {
            #'.':'',
            'newsletter_app':'run.py',
            'conf':'conf',
            'newsletter':'newsletter',
            'helpers':'helpers'
            },
        install_requires = [
            'Flask',
            'Flask-WTF',
            'flask-sqlalchemy',
            'mailchimp-marketing==3.0.44'],
        python_requires = '>=3.8'
        )


