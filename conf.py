# -*- coding: utf-8 -*-
AUTHOR = u'lrobot'
SITENAME = u"Lrobot blog"
SITESUBTITLE = u"Techtalk and stuff."
SITEURL = 'http://lrobot.me'
TIMEZONE = "Asia/Chongqing"
#THEME = 'bottle-theme'
FEED_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'
PDF_GENERATOR = False
REVERSE_CATEGORY_ORDER = True
LOCALE = "C"
DEFAULT_ORPHANS = 3
DEFAULT_PAGINATION = 10
DEFAULT_DATE = (2012, 03, 02, 14, 01, 01)

ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}.html'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}.html'
ARTICLE_LANG_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}-{lang}.html'
ARTICLE_LANG_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}-{lang}.html'
PAGE_URL = 'pages/{slug}.html'
PAGE_SAVE_AS = 'pages/{slug}.html'
PAGE_LANG_URL = 'pages/{slug}-{lang}.html'
PAGE_LANG_SAVE_AS = 'pages/{slug}-{lang}.html'

#GITHUB_URL = 'http://github.com/lrobot/lrobot.me'
#DISQUS_SITENAME = "bottlepy"
#TWITTER_USERNAME = "bottlepy"

MENUITEMS = (('Home','/'),)

LINKS = (('HOME','http://lrobot.me/'),)

SOCIAL = (('g+', 'https://plus.google.com/+QQLUO'),
          ('email', 'mailto:lrobot.qq@gmail.com'),)

# global metadata to all the contents
#DEFAULT_METADATA = (('yeah', 'it is'),)

# static paths will be copied under the same name
#STATIC_PATHS = ["static", ]

# A list of files to copy from the source to the destination
FILES_TO_COPY = (('static/robots.txt', 'robots.txt'),
                 ('static/favicon.ico', 'favicon.ico'),)

