#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'seb'
AUTHOR_EMAIL = u'seb@sebian.fr'
SITENAME = u"Seb's Peregrinations"
SITEURL = 'http://pelican.sebian.fr'
COVER_IMG_URL = 'http://badia.fr/img/ecrins.jpg'
#TAGLINE = 'foo'
#PROFILE_IMAGE_URL = 'http://badia.fr/img/sbadia.jpg'

TIMEZONE = 'Europe/Paris'
THEME = 'themes/pure'

from subprocess import check_output
VERSION_HASH = check_output(['git', 'rev-parse', '--short', 'HEAD']).strip()

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
TRANSLATION_FEED_ATOM = None
FEED_ALL_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'

# Retro-compat with my Old WP setup
ARTICLE_URL = '{slug}/'
ARTICLE_SAVE_AS = '{slug}/index.html'

# Blogroll
MENUITEMS = (('Home', 'http://pelican.sebian.fr'),
	    ('Ldn', "http://ldn-fai.net"),
	    ('Asrall', "http://planet.asrall.fr"),)

# Social widget
SOCIAL = (('twitter-square', 'http://twitter.com/sebastienbadia'),
          ('github', 'http://github.com/sbadia'),
          ('linkedin', 'http://fr.linkedin.com/in/sbadia'),
	 )

PLUGIN_PATH = 'plugins'
PLUGINS = ['gravatar']

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
