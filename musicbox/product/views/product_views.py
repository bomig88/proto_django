from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from config.containers import Services
from core.base.response_data import ResponseData
from product.views.serializers.product_serializer import ProductSerializer02

NM = "상품"
RES_LIST_NM = "products"
RES_DETAIL_NM = "product"

class ProductView(APIView):
    product_service = Services.product_service()

    @swagger_auto_schema(
        tags=[NM],
        operation_summary="{} 조회".format(NM),
        operation_description="{} 조회".format(NM),
        query_serializer=ProductSerializer02.GetParam(),
        responses={status.HTTP_200_OK: ProductSerializer02.GetResponse()}
    )
    def get(self, request: Request, **kwargs: dict) -> Response:
        """ 상품 목록 조회
        Args:
            request: 요청
            kwargs: path 파라미터
        Returns:
        """
        query_params = request.query_params.dict()

        serializer = self.product_service.select_all(params=query_params)

        return ResponseData.response_data(RES_LIST_NM, serializer.data, self.product_service.get_paginated_response())


    @swagger_auto_schema(
        tags=[NM],
        operation_summary="{} 등록".format(NM),
        operation_description="{} 등록".format(NM),
        request_body=ProductSerializer02.PostRequest(),
        responses={status.HTTP_200_OK: ProductSerializer02.PostResponse()}
    )
    def post(self, request: Request):
        """ 상품 등록
        Args:
            request: 요청
                request.data: 등록할 상품 정보
        Returns:
            등록된 상품 정보
        """
        serializer = self.product_service.create(request.data)

        return ResponseData.response_data(RES_DETAIL_NM, serializer.data)


class ProductDetailView(APIView):
    product_service = Services.product_service()

    @swagger_auto_schema(
        tags=[NM],
        operation_summary="{} 상세 조회".format(NM),
        operation_description="{} 상세 조회".format(NM),
        responses={status.HTTP_200_OK: ProductSerializer02.DetailGetResponse()}
    )
    def get(self, request: Request, **kwargs: dict) -> Response:
        """ 상품 상세 조회
        Args:
            request: 요청
            kwargs: path 파라미터
        Returns:
        """
        serializer = self.product_service.select(kwargs)

        return ResponseData.response_data(RES_DETAIL_NM, serializer.data)
