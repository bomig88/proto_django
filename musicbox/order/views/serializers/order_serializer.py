from rest_framework import serializers

from core.base.swagger_response_serializer import ResponseSerializer
from member.views.serializers.simplification.member_simplification_serializer import MemberSimplificationSerializer01
from order.filters.order_filter import OrderFilter
from order.models.order import Order
from order.serializers.simplification.order_product_simplification_serializer import \
    OrderProductSimplificationSerializer
from order.views.serializers.order_product_serializer import OrderProductSerializer02


class OrderSerializer01:
    """
    Swagger 주문 Serializer
    """
    class Default(serializers.ModelSerializer):
        class Meta:
            model = Order
            fields = '__all__'
            ref_name = __qualname__

    class List(serializers.ModelSerializer):
        member = MemberSimplificationSerializer01.Default(many=False)

        class Meta:
            model = Order
            fields = '__all__'
            ref_name = __qualname__

    class Detail(serializers.ModelSerializer):
        member = MemberSimplificationSerializer01.Default(many=False)
        order_products = OrderProductSimplificationSerializer(many=False)

        class Meta:
            model = Order
            fields = '__all__'
            ref_name = __qualname__

    class Field(serializers.Serializer):
        @staticmethod
        def seq(required=True):
            seq = serializers.IntegerField(
                required=required,
                help_text=Order.seq.field.help_text
            )
            return seq

        @staticmethod
        def member_seq(required=True):
            member_seq = serializers.IntegerField(
                required=required,
                help_text=Order.member_seq.field.help_text
            )
            return member_seq

        @staticmethod
        def status(required=True):
            status = serializers.ChoiceField(
                choices=tuple(Order.StatusChoice.choices),
                required=required,
                help_text=f'{Order.status.field.help_text} \ {str(Order.StatusChoice.choices)}'
            )
            return status

        @staticmethod
        def paid_at(required=True):
            paid_at = serializers.DateTimeField(
                required=required,
                help_text=Order.paid_at.field.help_text
            )
            return paid_at

        @staticmethod
        def sch_start_create_dt(required=True):
            sch_start_create_dt = serializers.DateTimeField(
                required=required,
                help_text=OrderFilter.base_filters['sch_start_create_dt'].field.help_text
            )
            return sch_start_create_dt

        @staticmethod
        def sch_end_create_dt(required=True):
            sch_end_create_dt = serializers.DateTimeField(
                required=required,
                help_text=OrderFilter.base_filters['sch_end_create_dt'].field.help_text
            )
            return sch_end_create_dt

        @staticmethod
        def ordering(required=False):
            ordering = serializers.ChoiceField(
                choices=list(OrderFilter.base_filters['ordering'].param_map.values()),
                required=required,
                help_text=OrderFilter.base_filters['ordering'].field.help_text
            )
            return ordering


class OrderSerializer02:
    """
    Swagger 주문 Serializer
    """
    class GetParam(serializers.Serializer):
        seq = OrderSerializer01.Field.seq(False)
        member_seq = OrderSerializer01.Field.member_seq(False)
        status = OrderSerializer01.Field.status(False)
        paid_at = OrderSerializer01.Field.paid_at(False)
        sch_start_create_dt = OrderSerializer01.Field.sch_start_create_dt(False)
        sch_end_create_dt = OrderSerializer01.Field.sch_end_create_dt(False)
        ordering = OrderSerializer01.Field.ordering(False)

        class Meta:
            ref_name = __qualname__

    class GetResponse(serializers.Serializer):
        orders = serializers.ListField(
            child=OrderSerializer01.List(),
            required=False,
            help_text="주문 목록"
        )

        class Meta:
            ref_name = __qualname__

    class DetailGetResponse(ResponseSerializer):
        class DetailGetResponseData(serializers.Serializer):
            order = OrderSerializer01.Detail(help_text="주문")

            class Meta:
                ref_name = __qualname__

        data = DetailGetResponseData(
            required=False,
            help_text="응답 데이터"
        )

        class Meta:
            ref_name = __qualname__

    class PostRequest(serializers.Serializer):
        order_products = OrderProductSerializer02.PostRequest(many=True)

        class Meta:
            ref_name = __qualname__

    class PostResponse(ResponseSerializer):

        class PostResponseData(serializers.Serializer):
            """
            주문 등록 응답 Serializer
            """
            order = OrderSerializer01.Detail(help_text="등록된 주문 정보")

            class Meta:
                ref_name = __qualname__

        data = PostResponseData(
            required=False,
            help_text="응답 데이터"
        )

        class Meta:
            ref_name = __qualname__

    class RefundPostRequest(serializers.Serializer):
        order_product_seqs = serializers.CharField(help_text='환불할 주문 상품들 일련번호, ","구분자')

        class Meta:
            ref_name = __qualname__

    class RefundPostResponse(ResponseSerializer):

        class RefundPostResponseData(serializers.Serializer):
            """
            주문 등록 응답 Serializer
            """
            order = OrderSerializer01.Detail(help_text="환불 처리된 주문 정보")

            class Meta:
                ref_name = __qualname__

        data = RefundPostResponseData(
            required=False,
            help_text="응답 데이터"
        )

        class Meta:
            ref_name = __qualname__
