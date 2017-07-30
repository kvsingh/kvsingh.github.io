#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Karanveer Singh'
SITENAME = u'Inhibited Zombies'
#SITEURL = 'https://kvsingh.github.io'
SITETITLE = 'Inhibited Zombies'

PATH = 'content'

TIMEZONE = 'Asia/Calcutta'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
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
PLUGINS = ['ipynb.markup']

#THEME = "/home/karan/pelican-themes/"
#THEME = "blueidea"
#THEME = "bulrush"
#THEME = "iris"

#THEME = "aboutwilson"
#THEME = "nikhil-theme"
#THEME = "tuxlite_tbs"
#THEME = "alchemy"

#THEME = "Flex"
THEME = "pure-single"

SOCIAL = (
        ('github', 'https://github.com/kvsingh/'),
        ('facebook', 'https://www.facebook.com/karanveer.singh1'),
        ('soundcloud', 'https://soundcloud.com/karanveer-singh-16'),
        ('linkedin' ,  'https://www.linkedin.com/in/karanveersingh/')
    )

#PYGMENTS = 'emacs'

IGNORE_FILES = ['.ipynb_checkpoints']
IPYNB_IGNORE_CSS=True
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
LOAD_CONTENT_CACHE = False
