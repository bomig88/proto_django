from django.urls import path


from member.views.views import TestView

urlpatterns = [
    path('test', TestView.as_view()),
]
