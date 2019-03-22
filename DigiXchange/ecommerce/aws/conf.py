import datetime, os
import boto3

AWS_ACCESS_KEY_ID = "AKIAJA6YIVYF2BLSFGSA"
AWS_SECRET_ACCESS_KEY = "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"

# AWS_S3_SIGNATURE_VERSION = "s3v4"
S3_USE_SIGV4 = True

AWS_GROUP_NAME = "DigiXchange_Group"
AWS_USERNAME = "alextaj"


# AWS_FILE_EXPIRE = 200
# AWS_PRELOAD_METADATA = True
AWS_QUERYSTRING_AUTH = False

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
AWS_STORAGE_BUCKET_NAME = 'digixchange'
AWS_S3_FILE_OVERWRITE=False
AWS_S3_HOST="s3.us-east-2.amazonaws.com"


# MEDIA_ROOT="https://s3.us-east-2.amazonaws.com/digixchange/media"
# STATIC_ROOT="https://s3.us-east-2.amazonaws.com/digixchange/static"





#
# S3DIRECT_REGION = 'us-east-2'
# S3_URL = '//%s.s3.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME
# MEDIA_URL = '//%s.s3.amazonaws.com/media/' % AWS_STORAGE_BUCKET_NAME
# # MEDIA_ROOT = MEDIA_URL
# STATIC_URL = S3_URL + 'static/'
# ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'
#
# two_months = datetime.timedelta(days=61)
# date_two_months_later = datetime.date.today() + two_months
# expires = date_two_months_later.strftime("%A, %d %B %Y 20:00:00 GMT")


# AWS_HEADERS = {
# 'Expires': expires,
# 'Cache-Control': 'max-age=%d' % (int(two_months.total_seconds()), ),
# }


# PROTECTED_DIR_NAME = 'protected'
# PROTECTED_MEDIA_URL = '//%s.s3.amazonaws.com/%s/' %( AWS_STORAGE_BUCKET_NAME, PROTECTED_DIR_NAME)
#
# AWS_DOWNLOAD_EXPIRE = 5000 #(0ptional, in milliseconds)

























# BACKE
