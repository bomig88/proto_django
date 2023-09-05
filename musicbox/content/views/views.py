from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from content.views.serializers.test_serializer import TestSerializer02
from _musicbox.containers import Services
from core.base.response_data import ResponseData

NM = '컨텐츠 테스트'
RES_LIST_NM = 'content_tests'
RES_DETAIL_NM = 'content_test'


class TestView(APIView):
    content_test_service = Services.content_test_service()

    @swagger_auto_schema(
        tags=[NM],
        operation_summary="{} 조회".format(NM),
        operation_description="{} 조회".format(NM),
        # query_serializer=TestSerializer02.GetParam(),
        responses={status.HTTP_200_OK: TestSerializer02.DetailGetResponse()}
    )
    def get(self, request: Request, **kwargs: dict) -> Response:
        """
        Args:
          kwargs: path 파라미터
        Returns:

        """
        query_params = request.query_params.dict()

        result = self.content_test_service.hello('content')

        return ResponseData.response_data(RES_DETAIL_NM, result)
