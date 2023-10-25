from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from _musicbox.containers import Services
from core.base.response_data import ResponseData
from order.views.serializers.order_serializer import OrderSerializer02

NM = "주문"
RES_LIST_NM = "orders"
RES_DETAIL_NM = "order"


class OrderView(APIView):
    order_service = Services.order_service()

    @swagger_auto_schema(
        tags=[NM],
        operation_summary="{} 조회".format(NM),
        operation_description="{} 조회".format(NM),
        query_serializer=OrderSerializer02.GetParam(),
        responses={status.HTTP_200_OK: OrderSerializer02.GetResponse()}
    )
    def get(self, request: Request, **kwargs: dict) -> Response:
        """
        Args:
            request: 요청
            kwargs: path 파라미터
        Returns:
        """
        query_params = request.query_params.dict()

        serializer = self.order_service.select_all(params=query_params)

        return ResponseData.response_data(RES_LIST_NM, serializer.data, self.order_service.get_paginated_response())

    @swagger_auto_schema(
        tags=[NM],
        operation_summary="{} 등록".format(NM),
        operation_description="{} 등록".format(NM),
        request_body=OrderSerializer02.PostRequest(),
        responses={status.HTTP_200_OK: OrderSerializer02.PostResponse()}
    )
    def post(self, request: Request):
        request_data = request.data
        request_data['member_seq'] = request.user.pk

        serializer = self.order_service.add(request_data)

        return ResponseData.response_data(RES_DETAIL_NM, serializer.data)


class OrderDetailView(APIView):
    order_service = Services.order_service()

    @swagger_auto_schema(
        tags=[NM],
        operation_summary="{} 상세 조회".format(NM),
        operation_description="{} 상세 조회".format(NM),
        responses={status.HTTP_200_OK: OrderSerializer02.DetailGetResponse()}
    )
    def get(self, request: Request, **kwargs: dict) -> Response:
        """
        Args:
            request: 요청
            kwargs: path 파라미터
        Returns:
        """
        serializer = self.order_service.select(kwargs)

        return ResponseData.response_data(RES_DETAIL_NM, serializer.data)


class OrderRefundView(APIView):
    order_service = Services.order_service()

    @swagger_auto_schema(
        tags=[NM],
        operation_summary="{} 환불".format(NM),
        operation_description="{} 환불".format(NM),
        request_body=OrderSerializer02.RefundPostRequest(),
        responses={status.HTTP_200_OK: OrderSerializer02.RefundPostResponse()}
    )
    def post(self, request: Request, **kwargs: dict):
        request_data = request.data
        request_data.update(kwargs)
        request_data['member_seq'] = request.user.pk

        serializer = self.order_service.refund(request_data)

        return ResponseData.response_data(RES_DETAIL_NM, serializer.data)
