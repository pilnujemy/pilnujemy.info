#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

AUTHOR = u'Adam Dobrawy'
SITENAME = u'Fundacja Pilnujemy.info'
SITEURL = 'localhost'
THEME = 'theme'
PATH = 'content'

TIMEZONE = 'Europe/Warsaw'

DEFAULT_LANG = u'pl'

# Feed generation is usually not desired when developing
FEED_DOMAIN = SITEURL

DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_CATEGORIES_ON_POST = True

# Blogroll
LINKS = (('Aktualności', '/'),
         ('Statut', '/pages/statut.html'),
         ('Kontakt', '/pages/kontakt.html'),
         ('GitHub', 'https://github.com/pilnujemy'),)

DEFAULT_PAGINATION = 10

PLUGIN_PATHS = ["plugins", ]
PLUGINS = ["post_revision.post_revision", "pin_to_top"]
# STATIC_PATHS = ['images', 'extra/CNAME']
# EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}

GITHUB_URL = "https://github.com/pilnujemy/pilnujemy.github.io"
GITHUB_BRANCH = "production"
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
