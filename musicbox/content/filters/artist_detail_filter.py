import django_filters

from content.models.artist_detail import ArtistDetail
from core.base.filter_set import FilterSet


class ArtistDetailFilter(FilterSet):
    # 일련번호
    field = ArtistDetail.seq.field
    oper_tp = FilterSet.Type.EXACT
    seq = django_filters.NumberFilter(
        field_name=field.name,
        lookup_expr=oper_tp,
        help_text=FilterSet.get_msg(field.help_text, oper_tp)
    )

    # 등록 시작일
    field = ArtistDetail.create_at.field
    oper_tp = FilterSet.Type.GTE
    sch_start_create_dt = django_filters.DateTimeFilter(
        field_name=field.name,
        lookup_expr=oper_tp,
        help_text=FilterSet.get_msg(field.help_text, oper_tp)
    )

    # 등록 종료일
    field = ArtistDetail.create_at.field
    oper_tp = FilterSet.Type.LTE
    sch_end_create_dt = django_filters.DateTimeFilter(
        field_name=field.name,
        lookup_expr=oper_tp,
        help_text=FilterSet.get_msg(field.help_text, oper_tp)
    )

    # 정렬 기준
    order_by_field = 'ordering'
    ordering = django_filters.OrderingFilter(
        fields=(
            'seq',
            '-seq',
        ),
        help_text="정렬 기준"
    )
