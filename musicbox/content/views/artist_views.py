from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from _musicbox.containers import Services
from content.views.serializers.artist_serializer import ArtistSerializer02
from core.base.response_data import ResponseData

NM = "아티스트"
RES_LIST_NM = "artists"
RES_DETAIL_NM = "artist"


class ArtistView(APIView):
    artist_service = Services.artist_service()

    @swagger_auto_schema(
        tags=[NM],
        operation_summary="{} 조회".format(NM),
        operation_description="{} 조회".format(NM),
        query_serializer=ArtistSerializer02.GetParam(),
        responses={status.HTTP_200_OK: ArtistSerializer02.GetResponse()}
    )
    def get(self, request: Request, **kwargs: dict) -> Response:
        """
        Args:
            request: 요청
            kwargs: path 파라미터
        Returns:
        """
        query_params = request.query_params.dict()

        serializer = self.artist_service.select_all(query_params)

        return ResponseData.response_data(RES_LIST_NM, serializer.data, self.artist_service.get_paginated_response())


class ArtistDetailView(APIView):
    artist_service = Services.artist_service()

    @swagger_auto_schema(
        tags=[NM],
        operation_summary="{} 상세 조회".format(NM),
        operation_description="{} 상세 조회".format(NM),
        responses={status.HTTP_200_OK: ArtistSerializer02.DetailGetResponse()}
    )
    def get(self, request: Request, **kwargs: dict) -> Response:
        """
        Args:
            request: 요청
            kwargs: path 파라미터
        Returns:
        """
        serializer = self.artist_service.select(kwargs)

        return ResponseData.response_data(RES_DETAIL_NM, serializer.data)

