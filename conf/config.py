from pytition.settings.base import *

SECRET_KEY = '__SECRET_KEY__'

STATIC_URL = '__PATH__/static/'
STATIC_ROOT = '__FINAL_PATH__/static'

MEDIA_URL = '__PATH__/mediaroot/'
MEDIA_ROOT = '__FINAL_PATH__/mediaroot'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '__DB_NAME__',
        'USER': '__DB_USER__',
        'PASSWORD': '__DB_PWD__',
        'HOST': '127.0.0.1',
    }
}

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', '[::1]', '__DOMAIN__']

#################################
#                               #
# DO NOT EDIT AFTER THIS BANNER #
#                               #
#################################

import os

# This needs to be redefined because STATIC_URL might be set in this config
# after TINYMCE_JS_URL was defined
TINYMCE_JS_URL = STATIC_URL + TINYMCE_JS_PATH

if DEFAULT_INDEX_THUMBNAIL == "":
    print("Please set a default index thumbnail or your index page will not be very beautiful")

# email backend
# Only supported configurations:
# - [default] no mailer backend, emails are sent synchronously with no retry if sending fails (USE_MAIL_QUEUE=False)
# - mailer backend used with uwsgi without cron jobs (USE_MAIL_QUEUE=True)
# - mailer backend used without uwsgi with cron jobs (USE_MAIL_QUEUE=True, MAIL_EXTERNAL_CRON_SET=True)
# Note: if MAIL_EXTERNAL_CRON_SET is set, the responsability to setup external cron job to send mail is up to the administrator.
# If none are set, the emails will never be send!
if USE_MAIL_QUEUE:
    INSTALLED_APPS += ('mailer',)
    # this enable mailer by default in django.send_email
    EMAIL_BACKEND = "mailer.backend.DbBackend"

if os.environ.get('DEBUG'):
    DEBUG = True
