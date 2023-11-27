from dependency_injector import containers, providers

from member.services.member_service import MemberService


class Services(containers.DeclarativeContainer):
    # member
    member_service = providers.Singleton(MemberService)
