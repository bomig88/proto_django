from django.contrib.auth.base_user import BaseUserManager


class BaseUserManager(BaseUserManager):

    def create_user(self, username, password=None):

        if username is None:
            raise TypeError('Users must have a username.')

        user = self.model(username=username)
        user.password = password
        user.status = 'join'
        user.save()

        return user

    def create_superuser(self, username, password):

        if password is None:
            raise TypeError('Superusers must have a password.')

        user = self.create_user(username, password)
        user.tag = user.TagChoice.SUPER_MANAGER.value
        user.save()

        return user
