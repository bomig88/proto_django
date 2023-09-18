import django_filters
from django_filters.widgets import CSVWidget

from content.models.album import Album
from core.base.filter_set import FilterSet


class AlbumFilter(FilterSet):
    """
    앨범 필터
    """
    # 일련번호
    field = Album.seq.field
    oper_tp = FilterSet.Type.EXACT
    seq = django_filters.NumberFilter(
        field_name=field.name,
        lookup_expr=oper_tp,
        help_text=FilterSet.get_msg(field.help_text, oper_tp)
    )

    # 아티스트 일련번호
    field = Album.artist_seq.field
    oper_tp = FilterSet.Type.EXACT
    artist_seq = django_filters.NumberFilter(
        field_name=field.name,
        lookup_expr=oper_tp,
        help_text=FilterSet.get_msg(field.help_text, oper_tp)
    )

    # 이름
    field = Album.name.field
    oper_tp = FilterSet.Type.ICONTAINS
    name = django_filters.CharFilter(
        field_name=field.name,
        lookup_expr=oper_tp,
        help_text=FilterSet.get_msg(field.help_text, oper_tp)
    )

    # 장르
    field = Album.genre.field
    oper_tp = FilterSet.Type.IN
    genre = django_filters.MultipleChoiceFilter(
        field_name=field.name,
        choices=tuple(Album.GenreChoices.choices),
        widget=CSVWidget,
        help_text=FilterSet.get_msg(field.help_text, oper_tp)
    )

    # 등록 시작일
    field = Album.create_at.field
    oper_tp = FilterSet.Type.GTE
    sch_start_create_dt = django_filters.DateTimeFilter(
        field_name=field.name,
        lookup_expr=oper_tp,
        help_text=FilterSet.get_msg(field.help_text, oper_tp)
    )

    # 등록 종료일
    field = Album.create_at.field
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
