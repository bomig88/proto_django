from dependency_injector import containers, providers

from content.services.test_services import ContentTestService
from member.services.test_services import MemberTestService


class Services(containers.DeclarativeContainer):
    content_test_service = providers.Singleton(ContentTestService)
    member_test_service = providers.Singleton(MemberTestService)
