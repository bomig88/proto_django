from dependency_injector import containers, providers

from member.services.member_service import MemberService
from product.services.product_service import ProductService
from seller.services.seller_service import SellerService


class Services(containers.DeclarativeContainer):
    # member
    member_service = providers.Singleton(MemberService)

    # product
    product_service = providers.Singleton(ProductService)

    # seller
    seller_service = providers.Singleton(SellerService)
