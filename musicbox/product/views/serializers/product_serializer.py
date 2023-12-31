from rest_framework import serializers

from core.base.swagger_response_serializer import PagingFieldSerializer, PagingResponseSerializer, ResponseSerializer
from product.filters.product_filter import ProductFilter
from product.models.product import Product


class ProductSerializer01:
    """
    Swagger 상품 Serializer
    """
    class Default(serializers.ModelSerializer):
        class Meta:
            model = Product
            fields = '__all__'
            ref_name = __qualname__

    class List(serializers.ModelSerializer):
        class Meta:
            model = Product
            fields = '__all__'
            ref_name = __qualname__

    class Detail(serializers.ModelSerializer):
        class Meta:
            model = Product
            fields = '__all__'
            ref_name = __qualname__

    class Field(serializers.Serializer):
        @staticmethod
        def seq(required=False):
            seq = serializers.IntegerField(
                required=required,
                help_text=Product.seq.field.help_text
            )
            return seq

        @staticmethod
        def seller_seq(required=False):
            seller_seq = serializers.IntegerField(
                required=required,
                help_text=Product.seller_seq.field.help_text
            )
            return seller_seq

        @staticmethod
        def name(required=False):
            name = serializers.CharField(
                required=required,
                help_text=Product.name.field.help_text
            )
            return name

        @staticmethod
        def representation_image(required=False):
            representation_image = serializers.CharField(
                required=required,
                help_text=Product.representation_image.field.help_text
            )
            return representation_image

        @staticmethod
        def org_price(required=False):
            org_price = serializers.IntegerField(
                required=required,
                help_text=Product.org_price.field.help_text
            )
            return org_price

        @staticmethod
        def sale_price(required=False):
            sale_price = serializers.IntegerField(
                required=required,
                help_text=Product.sale_price.field.help_text
            )
            return sale_price

        @staticmethod
        def discount_rate(required=False):
            discount_rate = serializers.IntegerField(
                required=required,
                help_text=Product.discount_rate.field.help_text
            )
            return discount_rate

        @staticmethod
        def tax_flag(required=False):
            tax_flag = serializers.IntegerField(
                required=required,
                help_text=Product.tax_flag.field.help_text
            )
            return tax_flag

        @staticmethod
        def counsel_telephone(required=False):
            counsel_telephone = serializers.CharField(
                required=required,
                help_text=Product.counsel_telephone.field.help_text
            )
            return counsel_telephone

        @staticmethod
        def status(required=False):
            status = serializers.ChoiceField(
                choices=tuple(Product.StatusChoice.choices),
                required=required,
                help_text=f'{Product.status.field.help_text} \ {str(Product.StatusChoice.choices)}'
            )
            return status

        @staticmethod
        def sch_start_create_dt(required=False):
            sch_start_create_dt = serializers.DateTimeField(
                required=required,
                help_text=ProductFilter.base_filters['sch_start_create_dt'].field.help_text
            )
            return sch_start_create_dt

        @staticmethod
        def sch_end_create_dt(required=False):
            sch_end_create_dt = serializers.DateTimeField(
                required=required,
                help_text=ProductFilter.base_filters['sch_end_create_dt'].field.help_text
            )
            return sch_end_create_dt

        @staticmethod
        def ordering(required=False):
            ordering = serializers.ChoiceField(
                choices=list(ProductFilter.base_filters['ordering'].param_map.values()),
                required=required,
                help_text=ProductFilter.base_filters['ordering'].field.help_text
            )
            return ordering


class ProductSerializer02:
    """
    Swagger 상품 Serializer
    """
    class GetParam(serializers.Serializer):
        seq = ProductSerializer01.Field.seq(required=False)
        seller_seq = ProductSerializer01.Field.seller_seq(required=False)
        name = ProductSerializer01.Field.name(required=False)
        tax_flag = ProductSerializer01.Field.tax_flag(required=False)
        status = ProductSerializer01.Field.status(required=False)
        sch_start_create_dt = ProductSerializer01.Field.sch_start_create_dt(required=False)
        sch_end_create_dt = ProductSerializer01.Field.sch_end_create_dt(required=False)

        page = PagingFieldSerializer.page(required=False)
        page_size = PagingFieldSerializer.page_size(required=False)

        ordering = ProductSerializer01.Field.ordering(required=False)

        class Meta:
            ref_name = __qualname__

    class GetResponse(PagingResponseSerializer):
        products = serializers.ListField(
            child=ProductSerializer01.List(),
            required=False,
            help_text='상품 목록'
        )

        class Meta:
            ref_name = __qualname__

    class DetailGetResponse(ResponseSerializer):
        class DetailGetResponseData(serializers.Serializer):
            seller = ProductSerializer01.Detail(help_text='상품')

            class Meta:
                ref_name = __qualname__

        data = DetailGetResponseData(
            required=False,
            help_text='응답 데이터'
        )

        class Meta:
            ref_name = __qualname__

    class PostRequest(serializers.Serializer):
        name = ProductSerializer01.Field.name(required=True)
        seller_seq = ProductSerializer01.Field.seller_seq(required=True)
        representation_image = ProductSerializer01.Field.representation_image(required=False)
        org_price = ProductSerializer01.Field.org_price(required=True)
        sale_price = ProductSerializer01.Field.sale_price(required=True)
        discount_rate = ProductSerializer01.Field.discount_rate(required=True)
        tax_flag = ProductSerializer01.Field.tax_flag(required=False)
        counsel_telephone = ProductSerializer01.Field.counsel_telephone(required=False)

        class Meta:
            ref_name = __qualname__

    class PostResponse(ResponseSerializer):
        class PostResponseData(serializers.Serializer):
            product = ProductSerializer01.Detail(help_text='등록된 상품 정보')

            class Meta:
                ref_name = __qualname__

        data = PostResponseData(
            required=False,
            help_text='응답 데이터'
        )

        class Meta:
            ref_name = __qualname__
