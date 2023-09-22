from rest_framework import permissions

from core.utils.logging_util import LoggingUtil


class IsAuthenticated(permissions.BasePermission):
    """
    API 메뉴 접근 권한 체크
    API 접속 로그 상세 기록 포함
    """
    logger = LoggingUtil()

    def has_permission(self, request, view):
        self.logger.info(f'login user = {request.user}')
        has_permission = request.user and request.user.is_authenticated
        return has_permission

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.create_by == request.user.username


class AllowAny(permissions.BasePermission):
    """
    API 메뉴 접근 권한 패스
    API 접속 로그 상세 기록 포함
    """
    # logger = LoggingUtil()
    def has_permission(self, request, view):
        return True
