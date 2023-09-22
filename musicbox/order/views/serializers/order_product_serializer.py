from rest_framework import serializers

from core.base.swagger_response_serializer import ResponseSerializer
from order.filters.order_product_filter import OrderProductFilter
from order.models.order_product import OrderProduct


class OrderProductSerializer01:
    """
    Swagger 주문 상품 Serializer
    """
    class Default(serializers.ModelSerializer):
        class Meta:
            model = OrderProduct
            fields = '__all__'
            ref_name = __qualname__

    class List(serializers.ModelSerializer):
        class Meta:
            model = OrderProduct
            fields = '__all__'
            ref_name = __qualname__

    class Detail(serializers.ModelSerializer):
        class Meta:
            model = OrderProduct
            fields = '__all__'
            ref_name = __qualname__

    class Field(serializers.Serializer):
        @staticmethod
        def seq(required=True):
            seq = serializers.IntegerField(
                required=required,
                help_text=OrderProduct.seq.field.help_text
            )
            return seq

        @staticmethod
        def order_seq(required=True):
            order_seq = serializers.IntegerField(
                required=required,
                help_text=OrderProduct.order_seq.field.help_text
            )
            return order_seq

        @staticmethod
        def music_seq(required=True):
            music_seq = serializers.IntegerField(
                required=required,
                help_text=OrderProduct.music_seq.field.help_text
            )
            return music_seq

        @staticmethod
        def status(required=True):
            status = serializers.ChoiceField(
                choices=tuple(OrderProduct.StatusChoice.choices),
                required=required,
                help_text=f'{OrderProduct.status.field.help_text} \ {str(OrderProduct.StatusChoice.choices)}'
            )
            return status

        @staticmethod
        def paid_at(required=True):
            paid_at = serializers.DateTimeField(
                required=required,
                help_text=OrderProduct.paid_at.field.help_text
            )
            return paid_at

        @staticmethod
        def sch_start_create_dt(required=True):
            sch_start_create_dt = serializers.DateTimeField(
                required=required,
                help_text=OrderProductFilter.base_filters['sch_start_create_dt'].field.help_text
            )
            return sch_start_create_dt

        @staticmethod
        def sch_end_create_dt(required=True):
            sch_end_create_dt = serializers.DateTimeField(
                required=required,
                help_text=OrderProductFilter.base_filters['sch_end_create_dt'].field.help_text
            )
            return sch_end_create_dt

        @staticmethod
        def ordering(required=False):
            ordering = serializers.ChoiceField(
                choices=list(OrderProductFilter.base_filters['ordering'].param_map.values()),
                required=required,
                help_text=OrderProductFilter.base_filters['ordering'].field.help_text
            )
            return ordering


class OrderProductSerializer02:
    """
    Swagger 주문 상품 Serializer
    """
    class GetParam(serializers.Serializer):
        seq = OrderProductSerializer01.Field.seq(False)
        order_seq = OrderProductSerializer01.Field.order_seq(False)
        status = OrderProductSerializer01.Field.status(False)
        paid_at = OrderProductSerializer01.Field.paid_at(False)
        sch_start_create_dt = OrderProductSerializer01.Field.sch_start_create_dt(False)
        sch_end_create_dt = OrderProductSerializer01.Field.sch_end_create_dt(False)
        ordering = OrderProductSerializer01.Field.ordering(False)

        class Meta:
            ref_name = __qualname__

    class GetResponse(serializers.Serializer):
        order_products = serializers.ListField(
            child=OrderProductSerializer01.List(),
            required=False,
            help_text="주문상품 목록"
        )

        class Meta:
            ref_name = __qualname__

    class DetailGetResponse(ResponseSerializer):
        class DetailGetResponseData(serializers.Serializer):
            order_product = OrderProductSerializer01.Detail(help_text="주문상품")

            class Meta:
                ref_name = __qualname__

        data = DetailGetResponseData(
            required=False,
            help_text="응답 데이터"
        )

        class Meta:
            ref_name = __qualname__

    class PostRequest(serializers.Serializer):
        music_seq = OrderProductSerializer01.Field.music_seq(required=True)

        class Meta:
            ref_name = __qualname__
