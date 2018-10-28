#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Karanveer Singh'
SITENAME = u'UnInhibited Zombie'
#SITEURL = 'https://kvsingh.github.io'
SITEURL = "http://localhost:8000"
SITETITLE = 'UnInhibited Zombie'

PATH = 'content'

TIMEZONE = 'Asia/Calcutta'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_DOMAIN = SITEURL
FEED_ALL_RSS = 'feeds/all.rss.xml'
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DISQUS_SITENAME = "inzombies"

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

GOOGLE_ANALYTICS = "UA-41437726-1"

DEFAULT_PAGINATION = 5

MARKUP = ('md', 'ipynb')

PLUGIN_PATH = './plugins'
PLUGINS = ['ipynb.markup', 'i18n_subsites', 'tag_cloud', 'cid_filters']

DISPLAY_PAGES_ON_MENU = True


#THEME = "Flex"
THEME = "pure-single"

JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}
NEST_HEADER_IMAGES = 'background.jpg'

#COLOR_SCHEME_CSS = "darkly.css"
#NEST_SOCIAL_COLUMN_TITLE = u'Social'


SOCIAL = (
        ('github', 'https://github.com/kvsingh/'),
        ('soundcloud', 'https://soundcloud.com/unzombie'),
        ('rss', 'https://kvsingh.github.io/feeds/all.rss.xml')
    )

PYGMENTS_STYLE = 'monokai'

IGNORE_FILES = ['.ipynb_checkpoints']
IPYNB_IGNORE_CSS=True
IPYNB_SKIP_CSS=True
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
LOAD_CONTENT_CACHE = False
