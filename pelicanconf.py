#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

AUTHOR = u'Adam Dobrawy'
SITENAME = u'Fundacja Pilnujemy.info'
SITEURL = 'http://pilnujemy.info'
THEME = 'theme'
PATH = 'content'

TIMEZONE = 'Europe/Warsaw'

DEFAULT_LANG = u'pl'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DISPLAY_PAGES_ON_MENU = True

# Blogroll
LINKS = (('Aktualności', '/'),
         ('Statut', '/pages/statut.html'),
         ('Kontakt', '/pages/kontakt.html'),
         ('GitHub', 'https://github.com/pilnujemy'),)

DEFAULT_PAGINATION = 10

PLUGIN_PATHS = ["plugins", ]
PLUGINS = ["post_revision.post_revision"]
# STATIC_PATHS = ['images', 'extra/CNAME']
# EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}


GITHUB_URL = "https://github.com/pilnujemy/pilnujemy.github.io"
GITHUB_BRANCH = "production"
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
