import os,sys,json
from easy_thumbnails.conf import Settings as thumbnail_settings

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '^c&91u5n2wpr6717u+(4wt0i)%cizz7=0p*=!jj+0o5hjlq!rk'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get("DEBUG")

ALLOWED_HOSTS = [
  'localhost',
  'interviews.localhost',
  '127.0.0.1',
  'ensaaf.backspace.com',
  'interviews.backspace.com',
  'graphonomy.com',
  'data.ensaaf.org',
  'interviews.ensaaf.org',
  ]


DEFAULT_HOST = 'data'
ROOT_URLCONF = 'ensaaf.urls'
ROOT_HOSTCONF = 'ensaaf.hosts'

SITE_ID = 1


# Application definition

INSTALLED_APPS = [
    'data.apps.DataConfig',
    'interviews.apps.InterviewsConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'easy_thumbnails',
    'image_cropping',
    'tinymce',
    'haystack',
    'django_hosts',
    'graphene_django',
    'admin_honeypot',
]

MIDDLEWARE = [
    'django_hosts.middleware.HostsRequestMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_hosts.middleware.HostsResponseMiddleware',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['data/templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'ensaaf.wsgi.application'


TINYMCE_DEFAULT_CONFIG = {
    "menubar": "edit view insert format",
    "plugins": "advlist autolink lists link charmap anchor searchreplace code",
    "toolbar": 'undo redo | styleselect | forecolor | bold italic | alignleft aligncenter alignright alignjustify | outdent indent | image link | removeformat',
    "valid_elements" : 'a[href|target=_blank],strong/b,div[align],i/em,u,br,p[align],h2,h3,h4,h5,span[style]',
    'statusbar': False,
    'height': 400,
    'media_live_embeds': False,
    'convert_urls': False,
    'relative_urls': False,
    'remove_script_host': False,
}


THUMBNAIL_PROCESSORS = (
    'image_cropping.thumbnail_processors.crop_corners',
) + thumbnail_settings.THUMBNAIL_PROCESSORS


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_PORT = 587

EMAIL_HOST = os.environ.get("EMAIL_HOST")
EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD")
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
SERVER_EMAIL = EMAIL_HOST_USER


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': '/var/tmp/django_capstat_cache',
        'TIMEOUT': 3600, # seconds, aka 1 hour
        'OPTIONS': { 'MAX_ENTRIES': 32768 }
    }
}



CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': '/var/tmp/django_cache',
    }
}

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'


# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.memcached.PyMemcacheCache',
#         'LOCATION': '127.0.0.1:11211',
#     }
# }


HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.solr_backend.SolrEngine',
        'URL': 'http://127.0.0.1:8983/solr/ensaaf',
        'ADMIN_URL': 'http://127.0.0.1:8983/solr/admin/cores',
        'TIMEOUT': 60 * 5,
        'INCLUDE_SPELLING': True,
        'BATCH_SIZE': 100,
    },
}


LOCALE_PATHS = [ 'data/locale' ]

GRAPHENE = { 'SCHEMA': 'data.schema.schema' }


# load a secrets file that isn't in source control; backup is using environ config
try:
    secrets = open(os.path.join(BASE_DIR, 'ensaaf/secrets.json'))
    jdata = json.load(secrets)
    for key,val in jdata.items():
        os.environ[key] = str(val)
except json.JSONDecodeError as jde:
    print("Exception while loading secrets.json: %s\n"%str(jde))
    sys.exit(1)
except OSError as ose:
    for each in ("DB_NAME","DB_USER","DB_PASSWD","DB_HOST","DB_PORT"):
        if not os.environ.get(each):
            print("Missing required credential %s from os.environ"%each)
            sys.exit(1)    
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/



INTERNAL_IPS = ('127.0.0.1', )


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get("DB_NAME"), 
        'USER': os.environ.get("DB_USER"), 
        'PASSWORD': os.environ.get("DB_PASSWD"), 
        'HOST': os.environ.get("DB_HOST"), 
        'PORT': os.environ.get("DB_PORT"), 
    }
}



# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

LANGUAGES = [
    ('pb', 'Punjabi'),
    ('en', 'English')
]

USE_I18N = True
USE_L10N = True

TIME_ZONE = 'UTC'
USE_TZ = True



STATIC_URL = '/static/'
STATICFILES_DIRS = ( os.path.join(BASE_DIR, "static/"), )
#STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, "media/") 



# super strict security
# when debug is "true", turn off strict security
USE_STRICT_SECURITY = not (DEBUG)
#SECURE_SSL_REDIRECT = USE_STRICT_SECURITY
SESSION_COOKIE_SECURE = USE_STRICT_SECURITY
CSRF_COOKIE_SECURE = USE_STRICT_SECURITY
SESSION_COOKIE_AGE = 3600 # 60 minutes expressed in seconds
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = 'DENY'
SECURE_HSTS_SECONDS = 3600 # 60 minutes expressed in seconds
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

