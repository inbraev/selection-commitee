from django.contrib.auth.models import BaseUserManager
from django.utils import timezone


class CustomUserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, is_active, is_staff,  is_superuser, **extra_fields):
        if email:
            email = self.normalize_email(email)
        now = timezone.now()
        user = self.model(
            email=email,
            is_active=is_active,
            is_staff=is_staff,
            is_superuser=is_superuser,
            last_login=now,
            created_at=now,
            **extra_fields
        )
        if password:
            user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        return self._create_user(email, password, True, True, False, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        return self._create_user(email, password, True, True, True, **extra_fields)
