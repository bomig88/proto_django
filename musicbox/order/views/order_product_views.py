from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from _musicbox.containers import Services
from core.base.response_data import ResponseData
from order.views.serializers.order_product_serializer import OrderProductSerializer02

NM = "주문상품"
RES_LIST_NM = "order_products"
RES_DETAIL_NM = "order_product"


class OrderProductView(APIView):
    order_product_service = Services.order_product_service()

    @swagger_auto_schema(
        tags=[NM],
        operation_summary="{} 조회".format(NM),
        operation_description="{} 조회".format(NM),
        query_serializer=OrderProductSerializer02.GetParam(),
        responses={status.HTTP_200_OK: OrderProductSerializer02.GetResponse()}
    )
    def get(self, request: Request, **kwargs: dict) -> Response:
        """
        Args:
            request: 요청
            kwargs: path 파라미터
        Returns:
        """
        query_params = request.query_params.dict()

        serializer = self.order_product_service.select_all(params=query_params)

        return ResponseData.response_data(RES_LIST_NM, serializer.data)


class OrderProductDetailView(APIView):
    order_product_service = Services.order_product_service()

    @swagger_auto_schema(
        tags=[NM],
        operation_summary="{} 상세 조회".format(NM),
        operation_description="{} 상세 조회".format(NM),
        responses={status.HTTP_200_OK: OrderProductSerializer02.DetailGetResponse()}
    )
    def get(self, request: Request, **kwargs: dict) -> Response:
        """
        Args:
            request: 요청
            kwargs: path 파라미터
        Returns:
        """
        serializer = self.order_product_service.select(kwargs)

        return ResponseData.response_data(RES_DETAIL_NM, serializer.data)

