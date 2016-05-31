#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

AUTHOR = u'Adam Dobrawy'
SITENAME = u'Pilnujemy.info'
SITEURL = 'localhost'
THEME = 'theme'
PATH = 'content'

TIMEZONE = 'Europe/Warsaw'

DEFAULT_LANG = 'pl'
LOCALE = ('pl_PL', 'pl_PL.UTF-8')

GOOGLE_ANALYTICS = 'UA-78574556-1'

# Feed generation is usually not desired when developing
FEED_DOMAIN = SITEURL

DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_CATEGORIES_ON_POST = False

# Blogroll
LINKS = (('Kontakt', '/pages/kontakt.html'),
         ('GitHub', 'https://github.com/pilnujemy'),
         ('Facebook', 'https://www.facebook.com/PilnujemyInfo-887008381347417/'),
         ('O nas', '/pages/o-nas.html'),
         ('Aktualności', '/'),
         )

DEFAULT_PAGINATION = 10

PLUGIN_PATHS = ["plugins", ]
PLUGINS = ["post_revision.post_revision", "pin_to_top", "sitemap", "neighbors"]
STATIC_PATHS = ['extra/favicons',
                'images',
                'extra/CNAME']
EXTRA_PATH_METADATA = {
                        'extra/favicons/': {'path': 'favicons'},
                        'extra/CNAME': {'path': 'CNAME'},
                        'extra/favicons/favicon.ico': {'path': 'favicon.ico'},
                        'extra/favicons/manifest.json': {'path': 'manifest.json'},
                        'extra/favicons/browserconfig.xml': {'path': 'browserconfig.xml'},
                    }

GITHUB_URL = "https://github.com/pilnujemy/pilnujemy.github.io"
GITHUB_BRANCH = "production"
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
