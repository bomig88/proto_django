from dependency_injector import containers, providers

from content.services.test_services import ContentTestService
from user.services.test_services import UserTestService


class Services(containers.DeclarativeContainer):
    content_test_service = providers.Singleton(ContentTestService)
    user_test_service = providers.Singleton(UserTestService)
