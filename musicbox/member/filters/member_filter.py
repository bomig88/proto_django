import django_filters
from django_filters.widgets import CSVWidget

from core.base.filter_set import FilterSet
from member.models.member import Member


class MemberFilter(FilterSet):
    """
    회원 필터
    """
    # 일련번호
    field = Member.seq.field
    oper_tp = FilterSet.Type.EXACT
    seq = django_filters.NumberFilter(
        field_name=field.name,
        lookup_expr=oper_tp,
        help_text=FilterSet.get_msg(field.help_text, oper_tp)
    )

    # 이름
    field = Member.username.field
    oper_tp = FilterSet.Type.ICONTAINS
    name = django_filters.CharFilter(
        field_name=field.name,
        lookup_expr=oper_tp,
        help_text=FilterSet.get_msg(field.help_text, oper_tp)
    )

    # 이메일
    field = Member.email.field
    oper_tp = FilterSet.Type.ICONTAINS
    email = django_filters.CharFilter(
        field_name=field.name,
        lookup_expr=oper_tp,
        help_text=FilterSet.get_msg(field.help_text, oper_tp)
    )

    # 분류
    field = Member.tag.field
    oper_tp = FilterSet.Type.IN
    tag = django_filters.MultipleChoiceFilter(
        field_name=field.name,
        choices=tuple(Member.TagChoice.choices),
        widget=CSVWidget,
        help_text=FilterSet.get_msg(field.help_text, oper_tp)
    )

    # 등록 시작일
    field = Member.create_at.field
    oper_tp = FilterSet.Type.GTE
    sch_start_create_dt = django_filters.DateTimeFilter(
        field_name=field.name,
        lookup_expr=oper_tp,
        help_text=FilterSet.get_msg(field.help_text, oper_tp)
    )

    # 등록 종료일
    field = Member.create_at.field
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
