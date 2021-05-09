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


class Parent(models.Model):
    first_name = models.CharField(max_length=50, blank=False, null=False, verbose_name='имя')
    second_name = models.CharField(max_length=50, blank=False, null=False, verbose_name='фамилия')
    middle_name = models.CharField(max_length=50, blank=False, null=False, verbose_name='отчество')
    job = models.CharField(max_length=100, blank=True, null=True, verbose_name='работа')
    position = models.CharField(max_length=100, blank=True, null=True, verbose_name='должность')
    phone = models.CharField(max_length=50, blank=True, null=True, verbose_name='телефон')
    email = models.EmailField(max_length=128, blank=True, null=True, verbose_name='почтовый адрес')
    student = models.OneToOneField(Student, blank=False, null=False, on_delete=models.CASCADE,
                                   verbose_name='абитуриент')
    address = models.OneToOneField(AddressParent, blank=False, null=False, on_delete=models.CASCADE,
                                   verbose_name='адрес')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')

    def __str__(self):
        return self.first_name

    class Meta:
        db_table = 'parent'
        verbose_name = 'Родители'
        verbose_name_plural = 'Родители'
        ordering = ('created_at',)


class OrtScoreInside(models.Model):
    basic_score = models.PositiveSmallIntegerField(default=0, blank=False, null=False, verbose_name='основной балл')
    bio_sub_score = models.PositiveSmallIntegerField(default=0, blank=False, null=False, verbose_name='биология')
    phy_sub_score = models.PositiveSmallIntegerField(default=0, blank=False, null=False, verbose_name='физика')
    chem_sub_score = models.PositiveSmallIntegerField(default=0, blank=False, null=False, verbose_name='химия')
    math_sub_score = models.PositiveSmallIntegerField(default=0, blank=False, null=False, verbose_name='математика')
    his_sub_score = models.PositiveSmallIntegerField(default=0, blank=False, null=False, verbose_name='история')
    eng_sub_score = models.PositiveSmallIntegerField(default=0, blank=False, null=False, verbose_name='англиский язык')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')

    def __str__(self):
        return f'{self.basic_score}'

    class Meta:
        db_table = 'ort_score_inside'
        verbose_name = 'Орт'
        verbose_name_plural = 'Орт'
        ordering = ('created_at',)


class EntryChallenge(models.Model):
    color = (
        ('1', 'Золотой'),
        ('2', 'Фиолетовый'),
        ('3', 'Желтый'),
        ('4', 'Голубой'),
        ('5', 'Красный'),
    )

    qualifying = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
    )

    qualifying_round_number = models.CharField(max_length=50, choices=qualifying, blank=False, null=False,
                                               verbose_name='номер отборочного тура')
    passed_ort = models.BooleanField(default=False, verbose_name='проходил орт')
    certificate_num = models.CharField(max_length=50, blank=True, null=True, verbose_name='номер сертификата')
    certificate_color = models.CharField(max_length=50, choices=color, blank=True, null=True,
                                         verbose_name='цвет сертификата')
    ort = models.OneToOneField(OrtScoreInside, blank=True, null=False, on_delete=models.CASCADE, verbose_name='орт')
    student = models.OneToOneField(Student, blank=False, null=False, on_delete=models.CASCADE,
                                   verbose_name='абитуриент')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')

    def __str__(self):
        return f'{self.passed_ort}'

    class Meta:
        db_table = 'entry_challenge'
        verbose_name = 'Вступительные испытание'
        verbose_name_plural = 'Вступительные испытание'
        ordering = ('created_at',)
