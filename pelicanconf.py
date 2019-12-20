#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Nathan West'
SITENAME = u'Vector Optimized Library of Kernels'
SITEURL = 'http://libvolk.org'
SITEMAP = {'format': 'xml'}

PATH = 'content'

TIMEZONE = 'US/Central'

DEFAULT_LANG = u'en'

THEME = 'volk-theme'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

#TEMPLATE_PAGES = {'news.html': 'news.html'}
DIRECT_TEMPLATES = ['index']

CACHE_CONTENT = False

PLUGIN_PATHS = ['plugins/pelican-bootstrapify', '/plugins/pelican-plugins']
PLUGINS = ['bootstrapify', 'sitemap', 'summary']

# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),
#         ('You can modify those links in your config file', '#'),)

# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
