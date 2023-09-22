from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView

from _musicbox.containers import Services
from member.views.serializers.auth_serializer import AuthSerializer02
from core.auth.base_permissions import AllowAny, IsAuthenticated
from core.auth.base_post_handle_authentication import BasePostHandleAuthentication
from core.base.response_data import ResponseData
from core.base.swagger_response_serializer import ResponseSerializer

TAG_NM = '인증'
NM = '인증'
RES_AUTH_NM = 'auth'


class AuthLoginView(APIView):
    """
        관리자 인증 View
    """

    permission_classes = [AllowAny]

    @swagger_auto_schema(
        tags=[NM],
        operation_summary=f"{NM} 로그인",
        operation_description=f"{NM} 로그인",
        request_body=AuthSerializer02.LoginPostRequest(),
        responses={status.HTTP_200_OK: AuthSerializer02.LoginPostResponse()}
    )
    def post(self, request: Request, **kwargs: dict) -> Response:
        """관리자 인증 함수입니다.
        Args:
            request: 요청 정보
            kwargs: path 파라미터
        Returns: 관리자 인증 응답
        """
        # 로그인 토큰 생성
        tokens = BasePostHandleAuthentication().token(request)

        return ResponseData.response_data(RES_AUTH_NM, tokens)


class AuthTokenVerifyView(TokenVerifyView):
    """
        관리자 인증 토큰 유효성 체크 View
    """

    @swagger_auto_schema(
        tags=[NM],
        operation_summary=f"{NM} 토큰 유효성 체크",
        operation_description=f"{NM} 토큰 유효성 체크",
        request_body=AuthSerializer02.TokenVerifyPostRequest(),
        responses={status.HTTP_200_OK: ResponseSerializer()}
    )
    def post(self, request: Request, **kwargs: dict) -> Response:
        """관리자 인증 토큰 유효성 체크 함수입니다.
        Args:
            request: 요청 정보
            kwargs: path 파라미터
        Returns: 관리자 인증 토큰 유효성 체크 응답
        """
        return Response(ResponseData.response(BasePostHandleAuthentication.token_verify(self, request.data)))


class AuthTokenRefreshView(TokenRefreshView):
    """
        관리자 인증 토큰 재발급 View
    """

    @swagger_auto_schema(
        tags=[NM],
        operation_summary=f"{NM} 토큰 재발급",
        operation_description=f"{NM} 토큰 재발급",
        request_body=AuthSerializer02.TokenRefreshPostRequest(),
        responses={status.HTTP_200_OK: AuthSerializer02.TokenRefreshPostResponse()}
    )
    def post(self, request: Request, **kwargs: dict) -> Response:
        """관리자 인증 토큰 재발급 함수입니다.
        Args:
            request: 요청 정보
            kwargs: path 파라미터
        Returns: 관리자 토큰 응답
        """
        return ResponseData.response_data(RES_AUTH_NM,
                                          BasePostHandleAuthentication.token_refresh(self, request.data))


class AuthLogoutView(APIView):
    @swagger_auto_schema(
        tags=[NM],
        operation_summary=f"{NM} 로그아웃",
        operation_description=f"{NM} 로그아웃",
        responses={status.HTTP_200_OK: ResponseSerializer()}
    )
    def post(self, request: Request):
        """ 관리자 로그아웃
        Args:
            request: 요청 정보
        Returns: 로그아웃 결과
        """
        return Response(ResponseData.response(BasePostHandleAuthentication().logout(request)))


class AuthApiPermissionTestView(APIView):
    permission_classes = [IsAuthenticated]

    MENU_NM = '테스트 목록 01'
    MENU_CD = 'AUTH001'

    RES_LIST_NM = 'managers'
    RES_DETAIL_NM = 'manager'
    member_service = Services.member_service()

    @swagger_auto_schema(
        tags=[TAG_NM],
        operation_summary="{} 테스트 목록 01".format(NM),
        operation_description="{} 테스트 목록 01".format(NM),
        query_serializer=AuthSerializer02.TestGetParam(),
        responses={status.HTTP_200_OK: AuthSerializer02.TestGetResponse()}
    )
    def get(self, request: Request, **kwargs: dict) -> Response:
        """리스트 조회 함수 입니다. (권한 체크 테스트용)
        Args:
            request: 요청 정보
            kwargs: path 파라미터
        Returns: 리스트 조회 응답
        """
        serializer = self.member_service.select_all(request.query_params.dict())

        return ResponseData.response_data(self.RES_LIST_NM, serializer.data)


class AuthApiPermissionDetailTestView(APIView):
    RES_DETAIL_NM = 'manager'

    permission_classes = [IsAuthenticated]

    MENU_NM = '테스트 상세 조회'
    MENU_CD = 'AUTH022'

    member_service = Services.member_service()

    @swagger_auto_schema(
        tags=[NM],
        operation_summary=f"{NM} 테스트 상세 조회",
        operation_description=f"{NM} 테스트 상세 조회",
        query_serializer=AuthSerializer02.TestDetailGetParam(),
        responses={status.HTTP_200_OK: AuthSerializer02.TestDetailGetResponse()}
    )
    def get(self, request: Request, **kwargs: dict) -> Response:
        """조회 함수 입니다. (권한 체크 테스트용)
        Args:
            request: 요청 정보
            kwargs: path 파라미터
        Returns: 조회 응답
        """
        serializer = self.member_service.select(kwargs)

        return ResponseData.response_data(self.RES_DETAIL_NM, serializer.data)


class AuthApiPermissionAnyTestView(APIView):
    RES_LIST_NM = 'managers'

    permission_classes = [AllowAny]

    MENU_NM = '테스트 목록 02'
    MENU_CD = 'AUTH003'

    member_service = Services.member_service()

    @swagger_auto_schema(
        tags=[TAG_NM],
        operation_summary="{} 테스트 목록 02".format(NM),
        operation_description="{} 테스트 목록 02".format(NM),
        query_serializer=AuthSerializer02.TestGetParam(),
        responses={status.HTTP_200_OK: AuthSerializer02.TestGetResponse()}
    )
    def get(self, request: Request, **kwargs: dict) -> Response:
        """관리자 리스트 조회 함수 입니다. (권한 체크 테스트용)
        Args:
            request: 요청 정보
            kwargs: path 파라미터
        Returns: 관리자 리스트 조회 응답
        """
        serializer = self.member_service.select_all(request.query_params.dict())

        return ResponseData.response_data(self.RES_LIST_NM, serializer.data)
