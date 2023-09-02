from django.urls import path


from user.views.views import TestView

urlpatterns = [
    path('test', TestView.as_view()),
]
