from rest_framework import serializers

from core.base.swagger_response_serializer import PagingFieldSerializer, PagingResponseSerializer, ResponseSerializer
from seller.filters.seller_filter import SellerFilter
from seller.models.seller import Seller


class SellerSerializer01:
    """
    Swagger 판매자 Serializer
    """
    class Default(serializers.ModelSerializer):
        class Meta:
            model = Seller
            fields = '__all__'
            ref_name = __qualname__

    class List(serializers.ModelSerializer):
        class Meta:
            model = Seller
            fields = '__all__'
            ref_name = __qualname__

    class Detail(serializers.ModelSerializer):
        class Meta:
            model = Seller
            fields = '__all__'
            ref_name = __qualname__

    class Field(serializers.Serializer):
        @staticmethod
        def seq(required=False):
            seq = serializers.IntegerField(
                required=required,
                help_text=Seller.seq.field.help_text
            )
            return seq

        @staticmethod
        def name(required=False):
            name = serializers.CharField(
                required=required,
                help_text=Seller.name.field.help_text
            )
            return name

        @staticmethod
        def representative(required=False):
            representative = serializers.CharField(
                required=required,
                help_text=Seller.representative.field.help_text
            )
            return representative

        @staticmethod
        def corporate_registration_number(required=False):
            corporate_registration_number = serializers.CharField(
                required=required,
                help_text=Seller.corporate_registration_number.field.help_text
            )
            return corporate_registration_number

        @staticmethod
        def business_registration_number(required=False):
            business_registration_number = serializers.CharField(
                required=required,
                help_text=Seller.business_registration_number.field.help_text
            )
            return business_registration_number

        @staticmethod
        def communication_seller_number(required=False):
            communication_seller_number = serializers.CharField(
                required=required,
                help_text=Seller.communication_seller_number.field.help_text
            )
            return communication_seller_number

        @staticmethod
        def customer_center(required=False):
            customer_center = serializers.CharField(
                required=required,
                help_text=Seller.customer_center.field.help_text
            )
            return customer_center

        @staticmethod
        def status(required=False):
            status = serializers.ChoiceField(
                choices=tuple(Seller.StatusChoice.choices),
                required=required,
                help_text=f'{Seller.status.field.help_text} \ {str(Seller.StatusChoice.choices)}'
            )
            return status

        @staticmethod
        def tag(required=False):
            tag = serializers.ChoiceField(
                choices=Seller.TagChoice.choices,
                required=required,
                help_text=f'{Seller.tag.field.help_text} \ {str(Seller.TagChoice.choices)}'
            )
            return tag

        @staticmethod
        def sch_start_create_dt(required=False):
            sch_start_create_dt = serializers.DateTimeField(
                required=required,
                help_text=SellerFilter.base_filters['sch_start_create_dt'].field.help_text
            )
            return sch_start_create_dt

        @staticmethod
        def sch_end_create_dt(required=False):
            sch_end_create_dt = serializers.DateTimeField(
                required=required,
                help_text=SellerFilter.base_filters['sch_end_create_dt'].field.help_text
            )
            return sch_end_create_dt

        @staticmethod
        def ordering(required=False):
            ordering = serializers.ChoiceField(
                choices=list(SellerFilter.base_filters['ordering'].param_map.values()),
                required=required,
                help_text=SellerFilter.base_filters['ordering'].field.help_text
            )
            return ordering


class SellerSerializer02:
    """
    Swagger 판매자 Serializer
    """
    class GetParam(serializers.Serializer):
        seq = SellerSerializer01.Field.seq(required=False)
        name = SellerSerializer01.Field.name(required=False)
        corporate_registration_number = SellerSerializer01.Field.corporate_registration_number(required=False)
        business_registration_number = SellerSerializer01.Field.business_registration_number(required=False)
        communication_seller_number = SellerSerializer01.Field.communication_seller_number(required=False)
        status = SellerSerializer01.Field.status(required=False)
        tag = SellerSerializer01.Field.tag(required=False)
        sch_start_create_dt = SellerSerializer01.Field.sch_start_create_dt(required=False)
        sch_end_create_dt = SellerSerializer01.Field.sch_end_create_dt(required=False)

        page = PagingFieldSerializer.page(required=False)
        page_size = PagingFieldSerializer.page_size(required=False)

        ordering = SellerSerializer01.Field.ordering(required=False)

        class Meta:
            ref_name = __qualname__

    class GetResponse(PagingResponseSerializer):
        sellers = serializers.ListField(
            child=SellerSerializer01.List(),
            required=False,
            help_text='판매자 목록'
        )

        class Meta:
            ref_name = __qualname__

    class DetailGetResponse(ResponseSerializer):
        class DetailGetResponseData(serializers.Serializer):
            seller = SellerSerializer01.Detail(help_text='판매자')

            class Meta:
                ref_name = __qualname__

        data = DetailGetResponseData(
            required=False,
            help_text='응답 데이터'
        )

        class Meta:
            ref_name = __qualname__

    class PostRequest(serializers.Serializer):
        name = SellerSerializer01.Field.name(required=True)
        representative = SellerSerializer01.Field.representative(required=True)
        corporate_registration_number = SellerSerializer01.Field.corporate_registration_number(required=False)
        business_registration_number = SellerSerializer01.Field.business_registration_number(required=False)
        communication_seller_number = SellerSerializer01.Field.communication_seller_number(required=False)
        customer_center = SellerSerializer01.Field.customer_center(required=True)
        tag = SellerSerializer01.Field.tag(required=False)

        class Meta:
            ref_name = __qualname__

    class PostResponse(ResponseSerializer):
        class PostResponseData(serializers.Serializer):
            seller = SellerSerializer01.Detail(help_text='등록된 판매자 정보')

            class Meta:
                ref_name = __qualname__

        data = PostResponseData(
            required=False,
            help_text='응답 데이터'
        )

        class Meta:
            ref_name = __qualname__
