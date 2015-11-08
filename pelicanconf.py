#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

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

DISPLAY_PAGES_ON_MENU = False

# Blogroll
LINKS = (('Aktualności', '/'),
         ('Statut', '/pages/statut.html'),
         ('Kontakt', '/pages/kontakt.html'),
         ('GitHub', 'https://github.com/pilnujemy'),)

DEFAULT_PAGINATION = 10

# STATIC_PATHS = ['images', 'extra/CNAME']
# EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}
