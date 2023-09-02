from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from user.views.serializers.test_serializer import TestSerializer02
from _musicbox.containers import Services
from utils.response_data import ResponseData

# Create your views here.

NM = '회원 테스트'
RES_LIST_NM = 'user_tests'
RES_DETAIL_NM = 'user_test'


class TestView(APIView):
    user_test_service = Services.user_test_service()

    @swagger_auto_schema(
        tags=[NM],
        operation_summary="{} 조회".format(NM),
        operation_description="{} 조회".format(NM),
        # query_serializer=TestSerializer02.GetParam(),
        responses={status.HTTP_200_OK: TestSerializer02.DetailGetResponse()}
    )
    def get(self, request: Request, **kwargs: dict) -> Response:
        """요청에 대한 쇼핑몰 상세를 반환합니다.
        Args:
          kwargs: path 파라미터
        Returns:
          쇼핑몰 상세 응답
        """
        query_params = request.query_params.dict()

        result = self.user_test_service.hello('user')

        return ResponseData.response_data(RES_DETAIL_NM, result)
