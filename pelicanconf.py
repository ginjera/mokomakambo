#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'ginjera'
SITENAME = u'Mokomakambo!'
SITEURL = 'http://ginjera.github.io/mokomakambo'

PATH = 'content'
STATIC_PATHS = ['images']

TIMEZONE = 'Asia/Singapore'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)

# Social widget
# SOCIAL = (('You can add links in your config file', '#'),
#           ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# Decode theme from Wordpress
# THEME = "pelican-themes/pelican-decode"
# THEME = "notmyidea"
# THEME = "pelican-themes/pelican-cait"
# THEME = "pelican-themes/pelican-blueidea"
# THEME = "pelican-themes/pelican-chunk"
# THEME = "pelican-themes/clean-master"
# THEME = "pelican-themes/bohemian-master"
THEME = "pelican-themes/flasky-master"

# code blocks with line numbers
PYGMENTS_RST_OPTIONS = {'linenos':'table'}

