from rest_framework import serializers


class ResponseSerializer(serializers.Serializer):
    """
    응답 Swagger Serializer
    """
    success = serializers.BooleanField(
        required=False,
        help_text="응답 성공 여부"
    )


class PagingFieldSerializer(serializers.Serializer):
    """
    페이징 필드 Swagger Serializer
    """
    @classmethod
    def current_page(cls, required=False):
        current_page = serializers.IntegerField(
            required=required,
            help_text='현재 페이지 수'
        )
        return current_page

    @classmethod
    def max_page(cls, required=False):
        max_page = serializers.IntegerField(
            required=required,
            help_text='최대 페이지 수'
        )
        return max_page

    @classmethod
    def page(cls, required=False):
        page = serializers.IntegerField(
            required=required,
            help_text='페이지 번호'
        )
        return page

    @classmethod
    def page_size(cls, required=False):
        page_size = serializers.IntegerField(
            required=required,
            help_text='페이지당 row 수'
        )
        return page_size

    @classmethod
    def row_num(cls, required=False):
        row_num = serializers.IntegerField(
            required=required,
            help_text='페이지당 row 수'
        )
        return row_num

    @classmethod
    def get_total_count_field(cls, required=False):
        total_count = serializers.IntegerField(
            required=required,
            help_text='전체 row 수'
        )
        return total_count


class PagingSerializer(serializers.Serializer):
    """
    페이징 Swagger Serializer
    """
    current_page = PagingFieldSerializer.current_page()
    max_page = PagingFieldSerializer.max_page()
    row_num = PagingFieldSerializer.row_num()
    total_count = PagingFieldSerializer.get_total_count_field()


class PagingResponseSerializer(ResponseSerializer):
    """
    페이징 포함 응답 Swagger Serializer
    """
    paging = PagingSerializer(
        required=False,
        help_text="페이징"
    )


class TypeSerializer(serializers.Serializer):
    """
        타입 Swagger Serializer
    """

    label = serializers.CharField(
        required=False,
        help_text='타입 한글명')

    value = serializers.CharField(
        required=False,
        help_text='타입')

    class Meta:
        ref_name = __qualname__


class TypeGetResponse(ResponseSerializer):
    """
    타입 응답 Serializer
    """
    class GetResponseData(serializers.Serializer):
        """
        타입 응답 data Serializer
        """
        types = serializers.ListField(
            child=TypeSerializer(),
            required=False,
            help_text="타입 리스트"
        )

        class Meta:
            ref_name = __qualname__

    data = GetResponseData(
        required=False,
        help_text="응답 데이터"
    )

    class Meta:
        ref_name = __qualname__
