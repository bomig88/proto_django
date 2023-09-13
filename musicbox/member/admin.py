from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.utils.translation import gettext_lazy as _

from member.models.member import Member


class MyMemberChangeForm(UserChangeForm):
    class Meta:
        model = Member
        fields = '__all__'


class MyMemberCreationForm(UserCreationForm):
    status = Member.StatusChoice.JOIN.value
    is_staff = False
    is_superuser = False

    class Meta:
        model = Member
        fields = ('email', 'username', 'status', 'gender', 'birthday')


@admin.register(Member)
class MyMemberAdmin(UserAdmin):
    model = Member
    readonly_fields = ['last_login_at', 'leave_at', 'create_at', 'update_at', 'status', 'is_active']
    fieldsets = (
        (None, {'fields': ('username', 'email', 'status', 'gender')}),
        (_('Permissions'), {'fields': ('is_active',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login_at', 'leave_at', 'create_at', 'update_at')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'gender', 'password1', 'password2'),
        }),
    )
    form = MyMemberChangeForm
    add_form = MyMemberCreationForm
    list_display = ('username', 'email', 'gender', 'status')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('email', 'username')
    ordering = ('email',)

