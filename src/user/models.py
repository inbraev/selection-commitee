from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin
)
from src.user.managers import CustomUserManager
from django.db import models
from src.subdivision.services import education


class Users(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=128, unique=True, blank=False, null=False, verbose_name='почтовый адрес')
    password = models.CharField(max_length=128, blank=False, null=False, verbose_name='пароль')
    is_active = models.BooleanField(default=True, verbose_name='активный пользователь')
    is_staff = models.BooleanField(default=True, blank=True, verbose_name='сотрудник')
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


class Commissioner(models.Model):
    first_name = models.CharField(max_length=50, blank=False, null=False, verbose_name='имя')
    second_name = models.CharField(max_length=50, blank=False, null=False, verbose_name='фамилия')
    middle_name = models.CharField(max_length=50, blank=False, null=False, verbose_name='отчество')
    user = models.OneToOneField(Users, blank=False, null=False, on_delete=models.CASCADE, verbose_name='пользователь')
    phone = models.CharField(max_length=50, blank=False, null=False, verbose_name='телефон')
    whats_app = models.CharField(max_length=50, blank=True, null=True, verbose_name='whatsapp')
    telegram = models.CharField(max_length=50, blank=True, null=True, verbose_name='telegram')
    instagram = models.CharField(max_length=50, blank=True, null=True, verbose_name='instagram')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')

    def __str__(self):
        return self.first_name

    class Meta:
        db_table = 'commissioner'
        verbose_name = 'Член приемной комиссии'
        verbose_name_plural = 'Члены приеной комисии'
        ordering = ('created_at',)


class PermissionCommissioner(models.Model):
    commissioner = models.ForeignKey(Commissioner, blank=False, null=False, on_delete=models.CASCADE,
                                     verbose_name='член комисии')
    education = models.CharField(max_length=50, choices=education, default='1', verbose_name='обучение')
    faculty = models.ForeignKey('subdivision.Faculty', blank=False, null=False, on_delete=models.CASCADE,
                                verbose_name='факультет')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')

    def __str__(self):
        return f'{self.commissioner}'

    class Meta:
        db_table = 'commissioner_permission'
        verbose_name = 'Доступ пользователя'
        verbose_name_plural = 'Доступ пользователей'
        ordering = ('created_at',)


class Student(models.Model):
    gender = (
        ('1', 'Мужчина'),
        ('2', 'Женщина'),
    )
    first_name = models.CharField(max_length=50, blank=False, null=False, verbose_name='имя')
    second_name = models.CharField(max_length=50, blank=False, null=False, verbose_name='фамилия')
    middle_name = models.CharField(max_length=50, blank=False, null=False, verbose_name='отчество')
    avatar = models.ImageField(blank=True, null=True, upload_to='student/avatar/', verbose_name='фото профиля')
    user = models.OneToOneField(Users, blank=False, null=False, on_delete=models.CASCADE, verbose_name='пользователь')
    sex = models.CharField(max_length=50, choices=gender, default='1', verbose_name='пол')
    phone = models.CharField(max_length=50, blank=False, null=False, verbose_name='телефон')
    dob = models.DateField(blank=False, null=False, verbose_name='день рождение')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')

    def __str__(self):
        return self.first_name

    class Meta:
        db_table = 'student'
        verbose_name = 'Абитуриент'
        verbose_name_plural = 'Абитуриенты'
        ordering = ('created_at',)
