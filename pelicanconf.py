#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from __future__ import print_function

AUTHOR = u'MonztA'
SITENAME = u'EasyList'
SITEURL = ''

PATH = 'content'
THEME = '.'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Main navigation
MENUITEMS = (
  ('Overview', '/index.html'),
  ('Articles', '/category/articles.html'),
  ('Development', '/pages/development.html'),
  ('Policy', '/pages/policy.html'),
  ('About', '/pages/about.html'),
  ('Forum', 'https://forums.lanik.us/'),
)

# Blogroll
LINKS = (
    ('EasyList', 'https://easylist.adblockplus.org/'),
)

# Social widget
SOCIAL = (
    ('EasyList Forum', 'https://forums.lanik.us/'),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
