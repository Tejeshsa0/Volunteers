from django.contrib.auth.base_user import BaseUserManager
from helper import messages

class UserManager(BaseUserManager):
    def _create_user(self, mobile, password, is_staff, is_superuser, **extra_fields):
        if not mobile:
            raise ValueError(messages.ENTER_VALID_NUMBER)
        user = self.model(
            mobile = mobile,
            is_staff = is_staff,
            is_active = True,
            is_superuser = is_superuser,
            **extra_fields
        )
        user.set_password(password)
        user.save(using = self._db)
        return user
    
    def create_user(self, mobile, password=None, **extra_fields):
        return self._create_user(mobile, password, False, False, **extra_fields)
    def create_superuser(self, mobile, password, **extra_fields):
        return self._create_user(mobile, password, True, True, **extra_fields)