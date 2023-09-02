from rest_framework import serializers

from utils.swagger_response_serializer import ResponseSerializer


class TestSerializer01:
    class Field(serializers.Serializer):
        """
        임시 파일 필드 Swagger Serializer
        """

        @staticmethod
        def url(required=True):
            url = serializers.CharField(
                required=required,
                help_text='단축할 URL'
            )
            return url


class TestSerializer02:
    class GetParam(serializers.Serializer):
        """
        단축 URL 조회 Serializer
        """
        url = TestSerializer01.Field.url()

        class Meta:
            ref_name = __qualname__

    class DetailGetResponse(ResponseSerializer):
        """
        단축 URL 조회 응답 Serializer
        """

        class DetailGetResponseData(serializers.Serializer):
            """
            단축 URL 조회 응답 data Serializer
            """

            test_code = serializers.CharField(help_text='test code')

            class Meta:
                ref_name = __qualname__

        data = DetailGetResponseData(
            required=False,
            help_text="응답 데이터"
        )

        class Meta:
            ref_name = __qualname__
