from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from _musicbox.containers import Services
from content.views.serializers.music_serializer import MusicSerializer02
from core.base.response_data import ResponseData

NM = "곡"
RES_LIST_NM = "musics"
RES_DETAIL_NM = "music"


class MusicView(APIView):
    music_service = Services.music_service()

    @swagger_auto_schema(
        tags=[NM],
        operation_summary="{} 조회".format(NM),
        operation_description="{} 조회".format(NM),
        query_serializer=MusicSerializer02.GetParam(),
        responses={status.HTTP_200_OK: MusicSerializer02.GetResponse()}
    )
    def get(self, request: Request, **kwargs: dict) -> Response:
        """
        Args:
            request: 요청
            kwargs: path 파라미터
        Returns:
        """
        query_params = request.query_params.dict()

        serializer = self.music_service.select_all(query_params)

        return ResponseData.response_data(RES_LIST_NM, serializer.data, self.music_service.get_paginated_response())


class MusicDetailView(APIView):
    music_service = Services.music_service()

    @swagger_auto_schema(
        tags=[NM],
        operation_summary="{} 상세 조회".format(NM),
        operation_description="{} 상세 조회".format(NM),
        responses={status.HTTP_200_OK: MusicSerializer02.DetailGetResponse()}
    )
    def get(self, request: Request, **kwargs: dict) -> Response:
        """
        Args:
            request: 요청
            kwargs: path 파라미터
        Returns:
        """
        serializer = self.music_service.select(kwargs)

        return ResponseData.response_data(RES_DETAIL_NM, serializer.data)

