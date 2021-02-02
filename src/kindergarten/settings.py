from pathlib import Path
import django_heroku

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '-#%zdu172m41begbu@cnw)b8k$5dn9@^408$kggc5&y78z3gqn'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    'localhost', 
    'kindergarten.herokuapp.com'
]

LOGIN_URL = '/racuni/prijava/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_URL = '/racuni/odjava/'

"""
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'kindergarten2021@gmail.com'
EMAIL_HOST_PASSWORD = 'qcrejnjsvyfcowgm'
EMAIL_USE_TLS = True
"""

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'vrtic.apps.VrticConfig',
    'financije.apps.FinancijeConfig',
    'dogadjaji.apps.DogadjajiConfig',
    'programi.apps.ProgramiConfig',
    'racuni.apps.RacuniConfig',
    'djeca.apps.DjecaConfig',
    'upisi.apps.UpisiConfig',
    'smjene.apps.SmjeneConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'kindergarten.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'kindergarten.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'local': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'kindergarten',
        'USER': 'postgres',
        'PASSWORD': 'user',
        'HOST': 'localhost'
    },
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'df3nnsseb06mro',
        'USER': 'cvvxlygafgryjr',
        'PASSWORD': '1e32e070cdcb3d12285bed93c71c80ea1e869d28331929d2e1ace921f23eebd5',
        'HOST': 'ec2-54-247-118-139.eu-west-1.compute.amazonaws.com'
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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

AUTHENTICATION_BACKENDS = [
    'racuni.backends.EmailBackend'
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'hr-HR'

TIME_ZONE = 'CET'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = '/staticfiles/'
STATICFILES_DIRS = (
    BASE_DIR / 'static',
)

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

django_heroku.settings(locals())
