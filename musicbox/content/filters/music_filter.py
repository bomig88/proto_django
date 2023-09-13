import django_filters

from content.models.music import Music
from core.base.filter_set import FilterSet


class MusicFilter(FilterSet):
    # 일련번호
    field = Music.seq.field
    oper_tp = FilterSet.Type.EXACT
    seq = django_filters.NumberFilter(
        field_name=field.name,
        lookup_expr=oper_tp,
        help_text=FilterSet.get_msg(field.help_text, oper_tp)
    )

    # 앨범 일련번호
    field = Music.album_seq.field
    oper_tp = FilterSet.Type.EXACT
    album_seq = django_filters.NumberFilter(
        field_name=field.name,
        lookup_expr=oper_tp,
        help_text=FilterSet.get_msg(field.help_text, oper_tp)
    )

    # 이름
    field = Music.name.field
    oper_tp = FilterSet.Type.ICONTAINS
    name = django_filters.CharFilter(
        field_name=field.name,
        lookup_expr=oper_tp,
        help_text=FilterSet.get_msg(field.help_text, oper_tp)
    )

    # 등록 시작일
    field = Music.create_at.field
    oper_tp = FilterSet.Type.GTE
    sch_start_create_dt = django_filters.DateTimeFilter(
        field_name=field.name,
        lookup_expr=oper_tp,
        help_text=FilterSet.get_msg(field.help_text, oper_tp)
    )

    # 등록 종료일
    field = Music.create_at.field
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
