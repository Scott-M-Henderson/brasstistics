# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys

sys.path.append(os.curdir)
from pelicanconf import *

# If your site is available via HTTPS, make sure SITEURL begins with https://
SITEURL = 'https://brasstistics.co.uk'
RELATIVE_URLS = False
DELETE_OUTPUT_DIRECTORY = True

OUTPUT_PATH = 'docs'
DEFAULT_PAGINATION = 10

FEED_ALL_ATOM = "feeds/all.atom.xml"
CATEGORY_FEED_ATOM = "feeds/{slug}.atom.xml"

DELETE_OUTPUT_DIRECTORY = True

THEME = 'themes/notmyidea-cms'

STATIC_PATHS = ['images', 'extra']

# Following items are often useful when publishing

# DISQUS_SITENAME = ""
# GOOGLE_ANALYTICS = ""
