#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'seb'
AUTHOR_EMAIL = u'seb@sebian.fr'
SITENAME = u"Seb's Peregrinations"
SITEURL = 'http://blog.sebian.fr'
COVER_IMG_URL = 'http://blog.sebian.fr/images/ecrins.jpg'
TAGLINE = 'DevOp & NetNeutrality'
#PROFILE_IMAGE_URL = 'http://badia.fr/img/sbadia.jpg'

TIMEZONE = 'Europe/Paris'
THEME = 'themes/pure'

from subprocess import check_output
VERSION_HASH = check_output(['git', 'rev-parse', '--short', 'HEAD']).strip()

# http://pygments.org/docs/lexers/#lexers-for-various-shells

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
TRANSLATION_FEED_ATOM = None
FEED_ALL_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'

# Retro-compat with my Old WP setup
ARTICLE_URL = '{slug}/'
ARTICLE_SAVE_AS = '{slug}/index.html'

# Blogroll
MENUITEMS = (('Archives', 'http://blog.sebian.fr/archives.html'),
             ('Ldn', 'http://ldn-fai.net'),
             ('Nybi.cc', 'http://nybi.cc/'),
             ('Asrall', 'http://planet.asrall.fr'),
            )

# Social widget
# http://fontawesome.io/icons/ (just remove « fa- »
SOCIAL = (('twitter-square', 'http://twitter.com/sebastienbadia'),
          ('github', 'http://github.com/sbadia'),
          ('linkedin', 'http://fr.linkedin.com/in/sbadia'),
          ('rss', 'http://blog.sebian.fr/feeds/all.rss.xml'),
         )

PLUGIN_PATHS = ['plugins']
PLUGINS = ['gravatar', 'neighbors']

STATIC_PATHS = ['images', 'extra']
EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/robots.txt': {'path': 'robots.txt'},
    }

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
