from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from _musicbox.containers import Services
from core.base.response_data import ResponseData
from member.views.serializers.member_serializer import MemberSerializer02

NM = "회원"
RES_LIST_NM = "members"
RES_DETAIL_NM = "member"


class MemberView(APIView):
    member_service = Services.member_service()

    @swagger_auto_schema(
        tags=[NM],
        operation_summary="{} 조회".format(NM),
        operation_description="{} 조회".format(NM),
        query_serializer=MemberSerializer02.GetParam(),
        responses={status.HTTP_200_OK: MemberSerializer02.GetResponse()}
    )
    def get(self, request: Request, **kwargs: dict) -> Response:
        """
        Args:
            request: 요청
            kwargs: path 파라미터
        Returns:
        """
        query_params = request.query_params.dict()

        serializer = self.member_service.select_all(params=query_params)

        return ResponseData.response_data(RES_LIST_NM, serializer.data)


class MemberDetailView(APIView):
    member_service = Services.member_service()

    @swagger_auto_schema(
        tags=[NM],
        operation_summary="{} 상세 조회".format(NM),
        operation_description="{} 상세 조회".format(NM),
        responses={status.HTTP_200_OK: MemberSerializer02.DetailGetResponse()}
    )
    def get(self, request: Request, **kwargs: dict) -> Response:
        """
        Args:
            request: 요청
            kwargs: path 파라미터
        Returns:
        """
        serializer = self.member_service.select(kwargs)

        return ResponseData.response_data(RES_DETAIL_NM, serializer.data)
