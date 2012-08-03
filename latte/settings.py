# Django settings for latte project.
import os

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'mydb.db',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Africa/Cairo'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = ''

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = ''

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Enable HTML compression
#COMPRESS_HTML = True

# Additional locations of static files
STATICFILES_DIRS = (     
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'v1i&&$rcw$)5%r%#ua15cjz_4@!n5oh@lc!w3o9v0isz1&4ep+'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
    "django.core.context_processors.request",
    'social_auth.context_processors.social_auth_by_name_backends',
    'social_auth.context_processors.social_auth_backends',
    'social_auth.context_processors.social_auth_by_type_backends',
    'social_auth.context_processors.social_auth_login_redirect',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.gzip.GZipMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    #'web.minify.html'
)

ROOT_URLCONF = 'latte.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'latte.wsgi.application'

TEMPLATE_DIRS = ( 
)

ACTSTREAM_ACTION_MODELS = ['auth.User', 'web.Item']

ACTSTREAM_MANAGER = 'actstream.managers.ActionManager'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.syndication.views',
    'bootstrap_toolkit',
    'web',
    'sitetree',
    'smarter',
    'taggit',
    'permissions',
    'userprofiles',
    'userprofiles.contrib.accountverification',    
    'userprofiles.contrib.emailverification',
    'userprofiles.contrib.profiles',
    'social_auth',
    'actstream',
    'endless_pagination'
)

AUTHENTICATION_BACKENDS = (
    'social_auth.backends.twitter.TwitterBackend',
    'social_auth.backends.facebook.FacebookBackend',
    'social_auth.backends.google.GoogleOAuthBackend',
    'social_auth.backends.google.GoogleOAuth2Backend',
    'social_auth.backends.google.GoogleBackend',
    'social_auth.backends.yahoo.YahooBackend',
    'social_auth.backends.browserid.BrowserIDBackend',
    'social_auth.backends.contrib.linkedin.LinkedinBackend',
    'social_auth.backends.contrib.livejournal.LiveJournalBackend',
    'social_auth.backends.contrib.orkut.OrkutBackend',
    'social_auth.backends.contrib.foursquare.FoursquareBackend',
    'social_auth.backends.contrib.github.GithubBackend',
    'social_auth.backends.contrib.dropbox.DropboxBackend',
    'social_auth.backends.contrib.flickr.FlickrBackend',
    'social_auth.backends.contrib.instagram.InstagramBackend',
#    'social_auth.backends.contrib.vkontakte.VkontakteBackend',
    'social_auth.backends.OpenIDBackend',
    'social_auth.backends.contrib.bitbucket.BitbucketBackend',
    'django.contrib.auth.backends.ModelBackend',
)

# Social Auth Settings
#LOGOUT_URL         = '/users/logout/'
#LOGIN_URL          = '/users/login/'
#SIGNIN_URL         = '/users/register/'
#LOGIN_REDIRECT_URL = '/users/%(username)s/'
#LOGIN_ERROR_URL    = '/users/login/error/'

SOCIAL_AUTH_PROTECTED_USER_FIELDS = ['email', 'username']
SOCIAL_AUTH_SESSION_EXPIRATION = False
SOCIAL_AUTH_USER_MODEL = 'auth.User'
SOCIAL_AUTH_ASSOCIATE_BY_MAIL = True
SOCIAL_AUTH_RAISE_EXCEPTIONS = DEBUG

SOCIAL_AUTH_NEW_USER_REDIRECT_URL        = '/welcome/'
SOCIAL_AUTH_NEW_ASSOCIATION_REDIRECT_URL = '/welcome/'
SOCIAL_AUTH_DISCONNECT_REDIRECT_URL      = '/welcome/'


TWITTER_CONSUMER_KEY         = 'ptPKKkaOWdAJ3Qbx0vHDA'
TWITTER_CONSUMER_SECRET      = 'TQ81NOssh1pXOH13TSv0bHNXRqZHEjllIuqJbXL2bw'
FACEBOOK_APP_ID              = '409051152453484'
FACEBOOK_API_SECRET          = '89127808f7c098a08b5cc3d94c7c53fe'
LINKEDIN_CONSUMER_KEY        = ''
LINKEDIN_CONSUMER_SECRET     = ''
ORKUT_CONSUMER_KEY           = ''
ORKUT_CONSUMER_SECRET        = ''
GOOGLE_CONSUMER_KEY          = ''
GOOGLE_CONSUMER_SECRET       = ''
GOOGLE_OAUTH2_CLIENT_ID      = '1089048547047.apps.googleusercontent.com'
GOOGLE_OAUTH2_CLIENT_SECRET  = '1d2MiUXEvbJiIB554P7-odty'
FOURSQUARE_CONSUMER_KEY      = ''
FOURSQUARE_CONSUMER_SECRET   = ''
GITHUB_APP_ID                = '8f04e91bd4c7deaa7c9a'
GITHUB_API_SECRET            = '65c26b0b782460a585e4f4e78caedec79d54e6b8'
DROPBOX_APP_ID               = ''
DROPBOX_API_SECRET           = ''
FLICKR_APP_ID                = ''
FLICKR_API_SECRET            = ''
INSTAGRAM_CLIENT_ID          = ''
INSTAGRAM_CLIENT_SECRET      = ''
VK_APP_ID                    = ''
VK_API_SECRET                = ''
BITBUCKET_CONSUMER_KEY       = ''
BITBUCKET_CONSUMER_SECRET    = ''

# Accounts Configuration
#USERPROFILES_CHECK_UNIQUE_EMAIL = True
#USERPROFILES_USE_ACCOUNT_VERIFICATION = True
#USERPROFILES_ACCOUNT_VERIFICATION_DAYS = 14
#USERPROFILES_INLINE_PROFILE_ADMIN = True
#USERPROFILES_REGISTRATION_FORM = 'web.forms.ProfileRegistrationForm'
USERPROFILES_USE_PROFILE = True
AUTH_PROFILE_MODULE = 'web.profile'

# Email Configuration
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'latte@gmail.com'
EMAIL_HOST_PASSWORD = 'XXXXXX'
EMAIL_PORT = 587

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}