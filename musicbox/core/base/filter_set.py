import django_filters
from django.db import models
from django.db.models import Q


class FilterSet(django_filters.FilterSet):

    # 필드, 조건 사이 구분자
    DELIMITER = '^'

    class Type(models.TextChoices):
        CONTAINS = 'contains', '을 포함(대소문자 구분)하는'
        ENDWITH = 'endwith', '으로 끝(대소문자 구분)나는'
        EQ = 'eq', '과 일치하는'
        EXACT = 'exact', '과 일치(대소문자 구분)하는'
        GT = 'gt', '큰'
        GTE = 'gte', '크거나 같은'
        ICONTAINS = 'icontains', '을 포함(대소문자 구분 없음)하는'
        IENDWITH = 'iendwith', '으로 끝(대소문자 구분 없음)나는'
        IEXACT = 'iexact', '과 일치(대소문자 구분 없음)하는'
        ISTARTSWITH = 'istartswith', '으로 시작(대소문자 구분 없음)하는'
        LT = 'lt', '작은'
        LTE = 'lte', '작거나 같은'
        STARTSWITH = 'startswith', '으로 시작(대소문자 구분)하는'
        IN = 'in', '속하는'

    def get_msg(self, filter_type, exclude=False) -> str:
        """Filter에 적용할 help_text 가져오기
        Args:
            self: 컬럼명
            filter_type: 필터 타입
            exclude: 대상 제외 여부
        Returns: help_text 값
        """

        # 대소 비교 타입
        comparison_type = [
            FilterSet.Type.GT.name,
            FilterSet.Type.GTE.name,
            FilterSet.Type.LT.name,
            FilterSet.Type.LTE.name
        ]

        if filter_type.name in comparison_type:
            msg = f'기준 값보다 {self}가 {filter_type.label} 경우'

        elif filter_type.name == FilterSet.Type.IN.name:
            msg = f'기준 값이 {self}에 {filter_type.label} 경우'

        else:
            msg = f'{self}이(가) 기준 값{filter_type.label} 경우'

        if exclude:
            msg = f"{msg} 제외"

        return msg

    @staticmethod
    def nullabe_with_method_(queryset, name_cond, value):
        """ null 여부를 포함된 조건문을 반환합니다.
        Args:
            queryset: 쿼리셋
            name_cond: 필드 및 조건
            value : 값
        Returns: 쿼리셋
        """
        filter_ = Q()
        vals = name_cond.split(FilterSet.DELIMITER)
        if len(vals) == 2:
            name = vals[0]
            cond = vals[1]

            if value == 'null':
                filter_.add(Q((f'{name}__isnull', True)), filter_.AND)
            elif value == 'notnull':
                filter_.add(Q((f'{name}__isnull', False)), filter_.AND)
            else:
                filter_.add(Q((f'{name}__{cond}', value)), filter_.AND)

        return queryset.filter(filter_)
