from datetime import timedelta

from _musicbox.settings.common import *

STAGE = "dev"
DEBUG = True

# simple jwt 설정
# TODO: ACCESS_TOKEN_LIFETIME 운영 반영 시점 때 시간값 정책 검토 필요 (현재는 테스트용 시간)
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(hours=10),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=30),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': False,
    'UPDATE_LAST_LOGIN': False,

    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'VERIFYING_KEY': None,
    'AUDIENCE': None,
    'ISSUER': None,
    'JWK_URL': None,
    'LEEWAY': 0,

    'AUTH_HEADER_TYPES': ('Bearer',),
    'USER_ID_FIELD': 'seq',
}

# LOGGING
#   disable_existing_loggers: 기존 로깅 비활성화 여부
#   formatters: 로그포맷
#   handlers: 로그 handler(로그 레코드로 어떤 작업을 할 것인지 정의)
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'formats': '%(asctime)s %(levelname)s[%(filename)s/line%(lineno)s]: %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S'
        },
        'sql': {
            '()': 'django_sqlformatter.SqlFormatter',
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
        'sql_': {
            'class': 'logging.StreamHandler',
            'formatter': SQL_FORMATTER,
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': False,
        },
        'django.db.backends': {
            'handlers': ['sql_'],
            'level': 'DEBUG',
            'propagate': False,
        },
    },
}
