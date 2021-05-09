from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin
)
from src.user.managers import CustomUserManager
from django.db import models


class Users(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=128, unique=True, blank=False, null=False, verbose_name='почтовый адрес')
    password = models.CharField(max_length=128, blank=False, null=False, verbose_name='пароль')
    is_active = models.BooleanField(default=True, verbose_name='активный пользователь')
    is_staff = models.BooleanField(default=False, blank=True, verbose_name='сотрудник')
    is_superuser = models.BooleanField(default=False, blank=True, verbose_name='администратор')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')

    USERNAME_FIELD = 'email'

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    class Meta:
        db_table = 'usr'
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('created_at',)
