from django.core.exceptions import ObjectDoesNotExist
from django.db.models import ProtectedError
from rest_framework.exceptions import ValidationError, ErrorDetail, NotAuthenticated, PermissionDenied
from rest_framework.response import Response
from rest_framework_simplejwt.exceptions import AuthenticationFailed, TokenError, InvalidToken
from core.utils.logging_util import LoggingUtil


class ResponseData:
    @staticmethod
    def response_data(name: str, data: object, paging: dict = None) -> Response:
        """응답 성공 데이터(dict)를 반환합니다.
        Args:
          name: 응답 데이터 key
          data: 응답 데이터
          paging: 페이징 데이터
        Returns:
          응답 성공 데이터(dict)
        """
        res_data = dict()
        res_data[name] = data

        return Response(ResponseData.response(True, res_data, paging))

    @staticmethod
    def response_fail_data(error: Exception) -> Response:
        """응답 실패 데이터(dict)를 반환합니다.
        Args:
          error: Exception
        Returns:
          응답 실패 데이터(dict)
        """
        logger = LoggingUtil()

        res_data = dict()

        if isinstance(error, ValidationError):
            message = ""
            system_message = ""

            if isinstance(error.detail, dict):
                # dict 내 key 정보로 ErrorDetail 확인
                keys = list(error.detail.keys())
                if keys:
                    message = f'{keys[0]} 정보를 확인해주세요.'
                    if isinstance(error.detail[keys[0]][0], ErrorDetail):
                        system_message = f'{error.detail[keys[0]][0].title()}({keys[0]})'
                    else:
                        system_message = f'{keys[0]} 정보를 확인해주세요.'
                else:
                    message = f'필수 파라미터 정보를 확인해주세요.'
                    system_message = f'필수 파라미터 정보를 확인해주세요.'

            elif isinstance(error.detail, list):
                # list 내 ErrorDetail 확인
                if error.detail and isinstance(error.detail[0], ErrorDetail):
                    message = f'{error.detail[0]} 정보를 확인해주세요.'
                    system_message = f'{error.detail[0].title()}'
                else:
                    message = f'필수 파라미터 정보를 확인해주세요.'
                    system_message = f'필수 파라미터 정보를 확인해주세요.'

            else:
                # serializer 내 모델 필드 딕셔너리
                fields = error.detail.serializer.fields
                for field, msg in error.detail.items():
                    message = f'{fields[field].help_text}(항목/필드명) 정보를 확인해주세요.'
                    system_message = f'{fields[field].help_text}({field}) {msg[0]}'
                    break

            res_data['message'] = message
            res_data['system_message'] = system_message

        # 요청한 데이터가 존재하지 않은 경우
        elif isinstance(error, ObjectDoesNotExist):
            res_data['system_message'] = "데이터가 존재하지 않습니다."
            res_data['message'] = "정보가 없습니다."

        # 인증 정보를 찾을 수 없는 경우
        elif isinstance(error, NotAuthenticated):
            res_data['system_message'] = '인증 정보를 찾을 수 없습니다.'
            res_data['message'] = "인증에 실패하였습니다."

        # 인증 실패한 경우
        elif isinstance(error, AuthenticationFailed) or isinstance(error, TokenError) \
                or isinstance(error, InvalidToken):
            res_data['system_message'] = error.detail['detail'] if 'detail' in error.detail else error.detail
            res_data['message'] = "인증에 실패하였습니다."

        # 권한이 없는 경우
        elif isinstance(error, PermissionDenied):
            res_data['system_message'] = '권한이 없습니다.'
            res_data['message'] = '권한이 없습니다.'

        # 모델 내 Protect 설정으로 인해 에러 발생한 경우
        elif isinstance(error, ProtectedError):
            res_data['system_message'] = error.args[0]
            res_data['message'] = '해당 요청건은 다른 데이터와 연결관계로 인해 수정이 불가합니다.'

            # 상품 관련 Protect 에러인 경우 별도 메세지 처리
            if error.args[0].find('Product') > -1:
                res_data['message'] = '해당 상품은 다른 데이터와 연결관계로 인해 수정이 불가합니다.'

        # 그 외
        else:
            res_data['system_message'] = error.args[0]
            res_data['message'] = '다시 확인해주세요.\n문제가 계속 될 경우 관리자센터로 문의바랍니다.'

            logger.error(f'에러 응답: {res_data}')
            logger.error(f'발생 에러: {error}')

        return Response(ResponseData.response(False, res_data))

    @staticmethod
    def response(success: bool, data: object = None, paging: dict = None) -> dict:
        """응답 데이터(dict)를 반환합니다.
        Args:
          success: 요청 결과
          data: 응답 데이터
          paging: 페이징 데이터
        Returns:
          응답 데이터(dict)
        """

        res = {}

        if success:
            # 정상 응답
            res['success'] = success
            if data:
                res['data'] = data
        else:
            # 에러
            res['success'] = success
            res['error'] = data

        if paging:
            res['paging'] = paging

        # print("###################################")
        # print("res")
        # print(res)
        # print("###################################")

        return res
