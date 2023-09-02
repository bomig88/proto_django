from _musicbox.settings.common import *

STAGE = "dev"
DEBUG = True

# LOGGING
#   disable_existing_loggers: 기존 로깅 비활성화 여부
#   formatters: 로그포맷
#   handlers: 로그 handler(로그 레코드로 어떤 작업을 할 것인지 정의)
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(asctime)s %(levelname)s[%(filename)s/line%(lineno)s]: %(message)s',
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
            'level': 'DEBUG',
            'propagate': False,
        },
        'django.db.backends': {
            'handlers': ['sql_'],
            'level': 'DEBUG',
            'propagate': False,
        },
    },
}
