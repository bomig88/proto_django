from django.contrib import admin
from django.http import HttpResponse
from django.urls import path, include, re_path

# drf-yasg Swagger
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_url_patterns = [
    path('contents/', include('content.urls')),
    path('members/', include('member.urls')),

]

# drf-yasg
schema_view = get_schema_view(
    openapi.Info(
        title="포트폴리오 API",
        default_version="v1",
        description="포트폴리오 API",
        terms_of_service="https://www.google.com/policies/terms/"
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
    patterns=schema_url_patterns
)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('contents/', include('content.urls')),
    path('members/', include('member.urls')),

    # default page
    path('', lambda request: HttpResponse("Hello world"), name="index"),

    # swagger
    re_path(r'^swagger(?P<formats>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
