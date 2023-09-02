from django.urls import path


from content.views.views import TestView

urlpatterns = [
    path('test', TestView.as_view()),
]
