from django.db import models


class Student(models.Model):
    gender = (
        ('1', 'Мужчина'),
        ('2', 'Женщина'),
    )
    first_name = models.CharField(max_length=50, blank=False, null=False, verbose_name='имя')
    second_name = models.CharField(max_length=50, blank=False, null=False, verbose_name='фамилия')
    middle_name = models.CharField(max_length=50, blank=False, null=False, verbose_name='отчество')
    avatar = models.ImageField(blank=True, null=True, upload_to='student/avatar/', verbose_name='фото профиля')
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


class AddressBirth(models.Model):
    republic = models.CharField(max_length=150, blank=False, null=False, default='Кыргызстан', verbose_name='страна')
    region = models.CharField(max_length=150, blank=False, null=False, default='Чуй', verbose_name='область')
    district = models.CharField(max_length=150, blank=False, null=False, default='Аламадунский', verbose_name='регион')
    city = models.CharField(max_length=150, blank=True, null=True, verbose_name='город')
    village = models.CharField(max_length=150, blank=True, null=True, verbose_name='село')
    student = models.OneToOneField(Student, blank=False, null=False, on_delete=models.CASCADE,
                                   verbose_name='абитуриент')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')

    def __str__(self):
        return self.republic

    class Meta:
        db_table = 'address_birth'
        verbose_name = 'Место рождения'
        verbose_name_plural = 'Место рождения'
        ordering = ('created_at',)


class AddressLiving(models.Model):
    republic = models.CharField(max_length=150, blank=False, null=False, default='Кыргызстан', verbose_name='страна')
    region = models.CharField(max_length=150, blank=False, null=False, default='Чуй', verbose_name='область')
    district = models.CharField(max_length=150, blank=False, null=False, default='Аламадунский', verbose_name='регион')
    city = models.CharField(max_length=150, blank=True, null=True, verbose_name='город')
    village = models.CharField(max_length=150, blank=True, null=True, verbose_name='село')
    phone = models.CharField(max_length=50, blank=True, null=True, verbose_name='телефон')
    student = models.OneToOneField(Student, blank=False, null=False, on_delete=models.CASCADE,
                                   verbose_name='абитуриент')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')

    def __str__(self):
        return self.republic

    class Meta:
        db_table = 'address_living'
        verbose_name = 'Место проживания'
        verbose_name_plural = 'Место проживания'
        ordering = ('created_at',)


class AddressResidence(models.Model):
    republic = models.CharField(max_length=150, blank=False, null=False, default='Кыргызстан', verbose_name='страна')
    region = models.CharField(max_length=150, blank=False, null=False, default='Чуй', verbose_name='область')
    district = models.CharField(max_length=150, blank=False, null=False, default='Аламадунский', verbose_name='регион')
    city = models.CharField(max_length=150, blank=True, null=True, verbose_name='город')
    village = models.CharField(max_length=150, blank=True, null=True, verbose_name='село')
    phone = models.CharField(max_length=50, blank=True, null=True, verbose_name='телефон')
    student = models.OneToOneField(Student, blank=False, null=False, on_delete=models.CASCADE,
                                   verbose_name='абитуриент')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')

    def __str__(self):
        return self.republic

    class Meta:
        db_table = 'address_residence'
        verbose_name = 'Место жительства'
        verbose_name_plural = 'Место жительства'
        ordering = ('created_at',)


class AddressParent(models.Model):
    republic = models.CharField(max_length=150, blank=False, null=False, default='Кыргызстан', verbose_name='страна')
    region = models.CharField(max_length=150, blank=False, null=False, default='Чуй', verbose_name='область')
    district = models.CharField(max_length=150, blank=False, null=False, default='Аламадунский', verbose_name='регион')
    city = models.CharField(max_length=150, blank=True, null=True, verbose_name='город')
    village = models.CharField(max_length=150, blank=True, null=True, verbose_name='село')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')

    def __str__(self):
        return self.republic

    class Meta:
        db_table = 'address_parent'
        verbose_name = 'Адрес родителей'
        verbose_name_plural = 'Адрес родителей'
        ordering = ('created_at',)
