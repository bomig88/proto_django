from django.urls import path


from member.views.member_views import MemberView, MemberDetailView, MemberRegisterView, MemberLeaveView

urlpatterns = [
    path('', MemberView.as_view()),
    path('<int:seq>', MemberDetailView.as_view()),
    path('<int:seq>/leave', MemberLeaveView.as_view()),
    path('register', MemberRegisterView.as_view())
]
