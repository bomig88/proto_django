from django.urls import path


from member.views.member_views import MemberView, MemberDetailView

urlpatterns = [
    path('', MemberView.as_view()),
    path('<int:seq>', MemberDetailView.as_view()),
]
