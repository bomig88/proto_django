from core.base.response_data import ResponseData


def custom_exception_handler(exc, context):
    return ResponseData.response_fail_data(exc)
