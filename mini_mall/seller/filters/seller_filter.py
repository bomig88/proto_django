import django_filters
from django_filters.widgets import CSVWidget

from core.base.filter_set import FilterSet
from seller.models.seller import Seller


class SellerFilter(FilterSet):
    """
    판매자 필터
    """
    # 일련번호
    field = Seller.seq.field
    oper_tp = FilterSet.Type.EXACT
    seq = django_filters.NumberFilter(
        field_name=field.name,
        lookup_expr=oper_tp,
        help_text=FilterSet.get_msg(field.help_text, oper_tp)
    )

    # 이름
    field = Seller.name.field
    oper_tp = FilterSet.Type.ICONTAINS
    name = django_filters.CharFilter(
        field_name=field.name,
        lookup_expr=oper_tp,
        help_text=FilterSet.get_msg(field.help_text, oper_tp)
    )

    # 대표자명
    field = Seller.representative.field
    oper_tp = FilterSet.Type.ICONTAINS
    representative = django_filters.CharFilter(
        field_name=field.name,
        lookup_expr=oper_tp,
        help_text=FilterSet.get_msg(field.help_text, oper_tp)
    )

    # 법인등록번호
    field = Seller.corporate_registration_number.field
    oper_tp = FilterSet.Type.ICONTAINS
    corporate_registration_number = django_filters.CharFilter(
        field_name=field.name,
        lookup_expr=oper_tp,
        help_text=FilterSet.get_msg(field.help_text, oper_tp)
    )

    # 사업자등록번호
    field = Seller.business_registration_number.field
    oper_tp = FilterSet.Type.ICONTAINS
    business_registration_number = django_filters.CharFilter(
        field_name=field.name,
        lookup_expr=oper_tp,
        help_text=FilterSet.get_msg(field.help_text, oper_tp)
    )

    # 통신판매업신고번호
    field = Seller.communication_seller_number.field
    oper_tp = FilterSet.Type.ICONTAINS
    communication_seller_number = django_filters.CharFilter(
        field_name=field.name,
        lookup_expr=oper_tp,
        help_text=FilterSet.get_msg(field.help_text, oper_tp)
    )

    # 상태
    field = Seller.status.field
    oper_tp = FilterSet.Type.IN
    status = django_filters.MultipleChoiceFilter(
        field_name=field.name,
        choices=tuple(Seller.StatusChoice.choices),
        widget=CSVWidget,
        help_text=FilterSet.get_msg(field.help_text, oper_tp)
    )

    # 분류
    field = Seller.tag.field
    oper_tp = FilterSet.Type.IN
    tag = django_filters.MultipleChoiceFilter(
        field_name=field.name,
        choices=tuple(Seller.TagChoice.choices),
        widget=CSVWidget,
        help_text=FilterSet.get_msg(field.help_text, oper_tp)
    )

    # 등록 시작일
    field = Seller.create_at.field
    oper_tp = FilterSet.Type.GTE
    sch_start_create_dt = django_filters.DateTimeFilter(
        field_name=field.name,
        lookup_expr=oper_tp,
        help_text=FilterSet.get_msg(field.help_text, oper_tp)
    )

    # 등록 종료일
    field = Seller.create_at.field
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
