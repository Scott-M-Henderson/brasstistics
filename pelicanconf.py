AUTHOR = 'Scott Henderson'
SITENAME = 'brasstistics'
SITEURL = 'https://brasstistics.co.uk'

PATH = 'content'
TIMEZONE = 'Europe/London'
DEFAULT_LANG = 'en'
OUTPUT_PATH = 'docs'

THEME = 'themes/notmyidea-cms'

DEFAULT_PAGINATION = 10
RELATIVE_URLS = True

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("YouTube", "https://www.youtube.com/@ScottTilYouDrop"),
)

STATIC_PATHS = ['images', 'extra']

EXTRA_PATH_METADATA = {
    'extra/BS_Logo.ico': {'path': 'favicon.ico'},
}

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
