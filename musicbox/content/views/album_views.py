from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from _musicbox.containers import Services
from content.views.serializers.album_serializer import AlbumSerializer02
from core.base.response_data import ResponseData

NM = "앨범"
RES_LIST_NM = "albums"
RES_DETAIL_NM = "album"


class AlbumView(APIView):
    album_service = Services.album_service()

    @swagger_auto_schema(
        tags=[NM],
        operation_summary="{} 조회".format(NM),
        operation_description="{} 조회".format(NM),
        query_serializer=AlbumSerializer02.GetParam(),
        responses={status.HTTP_200_OK: AlbumSerializer02.GetResponse()}
    )
    def get(self, request: Request, **kwargs: dict) -> Response:
        """
        Args:
            request: 요청
            kwargs: path 파라미터
        Returns:
        """
        query_params = request.query_params.dict()

        serializer = self.album_service.select_all(params=query_params)

        return ResponseData.response_data(RES_LIST_NM, serializer.data)


class AlbumDetailView(APIView):
    album_service = Services.album_service()

    @swagger_auto_schema(
        tags=[NM],
        operation_summary="{} 상세 조회".format(NM),
        operation_description="{} 상세 조회".format(NM),
        responses={status.HTTP_200_OK: AlbumSerializer02.DetailGetResponse()}
    )
    def get(self, request: Request, **kwargs: dict) -> Response:
        """
        Args:
            request: 요청
            kwargs: path 파라미터
        Returns:
        """
        serializer = self.album_service.select(kwargs)

        return ResponseData.response_data(RES_DETAIL_NM, serializer.data)

