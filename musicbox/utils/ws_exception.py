from rest_framework.views import exception_handler

from response_data import ResponseData


def custom_exception_handler(exc, context):
    # KeyError, Exception 등 CustomException이 아닌 다른 종류의 Error가 확인되지 않아 변경 by 박지민
    return ResponseData.response_fail_data(exc)
