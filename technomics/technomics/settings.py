# Django settings for technomics project.
import os
DEBUG = True
TEMPLATE_DEBUG = DEBUG


fillpath = lambda x: os.path.join(os.path.dirname(__file__), x)
ADMINS = (
    ('Shajeer', 'shajeer@technomicssolutions.com'),
    ('Vishnu', 'vishnu@technomicssolutions.com'),
    ('Remya', 'remya@technomicssolutions.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '',                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': '',
        'PASSWORD': '',
        'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    }
}

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'Asia/Kolkata'

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
# Full filesystem path to the project.
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

# Name of the directory for the project.
PROJECT_DIRNAME = PROJECT_ROOT.split(os.sep)[-1]
# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = fillpath('media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = '/site_media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = fillpath('static')


# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/'

# URL prefix for admin static files -- CSS, JavaScript and images.
# Make sure to use a trailing slash.
# Examples: "http://foo.com/static/admin/", "/static/admin/".
ADMIN_MEDIA_PREFIX = '/static/admin/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'j@7^xaw4p1euo!9r1@ph%pg7r2d4v4$%%@36l#9xz_h&2dtwm8'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.request',
    'django.core.context_processors.static',
    'technomics.context_processors.site_variables',
    'django.contrib.messages.context_processors.messages',
)

MIDDLEWARE_CLASSES = (
    'mediagenerator.middleware.MediaMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'technomics.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'technomics.wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

INSTALLED_APPS = (
    'web',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django_wsgiserver',
    'sorl.thumbnail',
    'mediagenerator',
    'south',
    'tinymce',
)

GENERATED_MEDIA_ROOT = fillpath('../_generated_media')
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

MEDIA_DEV_MODE = True
DEV_MEDIA_URL = '/devstatic/'
PRODUCTION_MEDIA_URL = '/static/'

GLOBAL_MEDIA_DIRS = () #(os.path.join(os.path.dirname(__file__), 'static'),)


MEDIA_BUNDLES = (
    ('main.css',
        'less/style.less', 
        'less/slideshow.less',       
    ),    
    ('mootools.js',
        {'filter': 'mediagenerator.filters.media_url.MediaURL'},
        'js/mootools-core-1.4.2-full-compat-yc.js',
        'js/mootools-more-1.4.0.1.js',        
    ),
    ('main.js',
        'js/contact_form.js',
        'js/slideshow.js',
    ),
)

ROOT_MEDIA_FILTERS = {
    'js': 'mediagenerator.filters.yuicompressor.YUICompressor',
    'css': 'mediagenerator.filters.yuicompressor.YUICompressor',
}

YUICOMPRESSOR_PATH = os.path.join(os.path.dirname(__file__), '../tools', 'yuicompressor-2.4.6.jar')
print YUICOMPRESSOR_PATH
TINYMCE_JS_URL= (MEDIA_URL + 'js/tiny_mce/tiny_mce.js')
    #The URL of the TinyMCE javascript file.
TINYMCE_JS_ROOT = (MEDIA_ROOT + '/js/tiny_mce')
    #The filesystem location of the TinyMCE files.
# TINYMCE_DEFAULT_CONFIG = ({'theme': "advanced", 'relative_urls': False,
TINYMCE_DEFAULT_CONFIG = ({'theme': "advanced", 'relative_urls': False,
                        'theme_advanced_disable' : "styleselect",
                        'theme_advanced_toolbar_location' : "top",
                        'plugins' : "paste",
                        'theme_advanced_buttons3_add' : "pastetext,pasteword,selectall",
                        'paste_auto_cleanup_on_paste' : True,})
    #The default TinyMCE configuration to use. See the TinyMCE manual for all options. To set the configuration for a specific TinyMCE editor, see the mce_attrs parameter for the widget.
TINYMCE_SPELLCHECKER = False
    #Whether to use the spell checker through the supplied view. You must add spellchecker to the TinyMCE plugin list yourself, it is not added automatically.
TINYMCE_COMPRESSOR = False
    #Whether to use the TinyMCE compressor, which gzips all Javascript files into a single stream. This makes the overall download size 75% smaller and also reduces the number of requests. The overall initialization time for TinyMCE will be reduced dramatically if you use this option.
#TINYMCE_FILEBROWSER (True if 'filebrowser' in INSTALLED_APPS, else False)

try:
   from local_settings import *
except:
   pass
