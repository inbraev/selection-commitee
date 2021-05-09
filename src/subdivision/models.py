from django.db import models


class Vuz(models.Model):
    name = models.CharField(max_length=255, unique=True, blank=False, null=False, verbose_name='название')
    short_name = models.CharField(max_length=100, unique=True, blank=False, null=False, verbose_name='краткое название')
    address = models.CharField(max_length=255, blank=False, null=False, verbose_name='адрес')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'vuz'
        verbose_name = 'Вуз'
        verbose_name_plural = 'Вузы'
        ordering = ('created_at',)


class Faculty(models.Model):
    name = models.CharField(max_length=255, unique=True, blank=False, null=False, verbose_name='название')
    short_name = models.CharField(max_length=100, unique=True, blank=False, null=False, verbose_name='краткое название')
    vuz = models.ForeignKey(Vuz, blank=False, null=False, on_delete=models.CASCADE, verbose_name='вуз')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'faculty'
        verbose_name = 'Факультет'
        verbose_name_plural = 'Факультеты'
        ordering = ('created_at',)


class Direction(models.Model):
    cipher = models.CharField(max_length=255, unique=True, blank=False, null=False, verbose_name='шифр')
    name = models.CharField(max_length=255, unique=True, blank=False, null=False, verbose_name='название')
    faculty = models.ForeignKey(Faculty, blank=False, null=False, on_delete=models.CASCADE, verbose_name='факультет')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'direction'
        verbose_name = 'Направление'
        verbose_name_plural = 'Направлении'
        ordering = ('created_at',)


class Section(models.Model):
    name = models.CharField(max_length=255, unique=True, blank=False, null=False, verbose_name='название')
    direction = models.ForeignKey(Direction, blank=False, null=False, on_delete=models.CASCADE,
                                  verbose_name='направление')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'section'
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
        ordering = ('created_at',)
