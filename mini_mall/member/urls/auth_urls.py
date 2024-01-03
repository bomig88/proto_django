from django.urls import path


from member.views.auth_views import (AuthLoginView, AuthLogoutView, AuthTokenRefreshView, AuthTokenVerifyView,
                                     AuthApiPermissionTestView, AuthApiPermissionDetailTestView,
                                     AuthApiPermissionAnyTestView)

urlpatterns = [
    path('/login', AuthLoginView.as_view()),
    path('/logout', AuthLogoutView.as_view()),
    path('/token/verify', AuthTokenVerifyView.as_view()),
    path('/token/refresh', AuthTokenRefreshView.as_view()),

    # API 사용자 접근 권한 테스트 용
    path('/permission_test', AuthApiPermissionTestView.as_view()),
    path('/permission_test/<int:seq>', AuthApiPermissionDetailTestView.as_view()),
    path('/permission_any_test', AuthApiPermissionAnyTestView.as_view()),
]
