import django_filters
from django_filters.widgets import CSVWidget

from core.base.filter_set import FilterSet
from order.models.order_product import OrderProduct


class OrderProductFilter(FilterSet):
    # 일련번호
    field = OrderProduct.seq.field
    oper_tp = FilterSet.Type.EXACT
    seq = django_filters.NumberFilter(
        field_name=field.name,
        lookup_expr=oper_tp,
        help_text=FilterSet.get_msg(field.help_text, oper_tp)
    )

    # 주문 일련번호
    field = OrderProduct.order_seq.field
    oper_tp = FilterSet.Type.EXACT
    order_seq = django_filters.NumberFilter(
        field_name=field.name,
        lookup_expr=oper_tp,
        help_text=FilterSet.get_msg(field.help_text, oper_tp)
    )

    # 상태
    field = OrderProduct.status.field
    oper_tp = FilterSet.Type.IN
    status = django_filters.MultipleChoiceFilter(
        field_name=field.name,
        choices=tuple(OrderProduct.StatusChoice.choices),
        widget=CSVWidget,
        help_text=FilterSet.get_msg(field.help_text, oper_tp)
    )

    # 등록 시작일
    field = OrderProduct.create_at.field
    oper_tp = FilterSet.Type.GTE
    sch_start_create_dt = django_filters.DateTimeFilter(
        field_name=field.name,
        lookup_expr=oper_tp,
        help_text=FilterSet.get_msg(field.help_text, oper_tp)
    )

    # 등록 종료일
    field = OrderProduct.create_at.field
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
