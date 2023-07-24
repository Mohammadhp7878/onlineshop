from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, phone_number,password=None, **kwargs):
        if not phone_number:
            raise ValueError('phone number is required')
        user.set_password(password)
        user = self.model(phone_number=phone_number, **kwargs)
        user.save(using=self._db)

    def create_superuser(self, phone_number, password, **kwargs):
        if not password:
            raise ValueError('Password is required for superuser')
        user = self.create_user(phone_number, password=password, **kwargs)
        user.is_admin = True
        user.save(using=self._db)
