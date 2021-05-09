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


class Percs(models.Model):
    orphan = models.BooleanField(default=False,
                                 verbose_name='Круглый сирота')
    ethnical_kyrgyz = models.BooleanField(default=False,
                                          verbose_name='Этнический кыргыз')
    care = models.BooleanField(default=False,
                               verbose_name='На попечении')
    invalid = models.BooleanField(default=False,
                                  verbose_name='Инвалид 1 или 2 группы')
    student = models.OneToOneField(Student, blank=False, null=False, on_delete=models.CASCADE,
                                   verbose_name='Абитуриент')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')

    def __str__(self):
        return f'{self.student}'

    class Meta:
        db_table = 'percs'
        verbose_name = 'Льготник'
        verbose_name_plural = 'Льготники'
        ordering = ('created_at',)


class Passport(models.Model):
    status = (
        ('1', 'Не состоит в браке'),
        ('2', 'Женат/замужем'),

    )
    inn = models.IntegerField(blank=False, null=False, default='23003199920251', verbose_name='ИНН')
    serial_number = models.CharField(blank=False, max_length=50, null=False, default='AN192502',
                                     verbose_name='Серия паспорта')
    family_status = models.CharField(max_length=50, choices=status, default='1',
                                     verbose_name='Семейное положение')
    citizenship = models.CharField(max_length=150, blank=False, null=False, default='Кыргызстан',
                                   verbose_name='Гражданство')
    get_date = models.DateField(blank=False, null=False, verbose_name='Дата выдачи')
    issuing_auth = models.CharField(max_length=150, blank=False, null=False, default='MKK 50-55',
                                    verbose_name='Кем выдан')
    student = models.OneToOneField(Student, blank=False, null=False, on_delete=models.CASCADE,
                                   verbose_name='Абитуриент')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')

    def __str__(self):
        return f'{self.inn}'

    class Meta:
        db_table = 'passport'
        verbose_name = 'Паспорт'
        verbose_name_plural = 'Паспорты'
        ordering = ('created_at',)


class MilitaryService(models.Model):
    documents = (
        ('1', 'Приписное свидетельство'),
        ('2', 'Военный билет'),
    )
    document = models.CharField(max_length=50, choices=documents, default='1',
                                verbose_name='Документ')
    serial_number = models.CharField(blank=True, max_length=50, null=True, verbose_name='Серия №')
    name_of_military_regis = models.CharField(blank=True, max_length=50, null=True,
                                              verbose_name='Название воинского учета')
    military_registration_date = models.DateField(blank=True, null=True, verbose_name='Дата воинского учета')
    good = models.BooleanField(default=False,
                               verbose_name='Годен к службе')
    special_account = models.BooleanField(default=False,
                                          verbose_name='Состоит на спецучете')
    special_account_number = models.CharField(max_length=150, blank=True, null=True,
                                              verbose_name='Номер спецучета')
    transferred_to_the_reserve = models.BooleanField(default=False,
                                                     verbose_name='Уволен в запас')
    rank = models.CharField(max_length=150, blank=True, null=True,
                            verbose_name='Звание')
    military_registration_speciality = models.CharField(max_length=150, blank=True, null=True,
                                                        verbose_name='Военно-учетная специальность')
    military_registration_number = models.CharField(max_length=150, blank=True, null=True,
                                                    verbose_name='Номер военно-учетной специальности')
    student = models.OneToOneField(Student, blank=False, null=False, on_delete=models.CASCADE,
                                   verbose_name='Абитуриент')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')

    def __str__(self):
        return self.document

    class Meta:
        db_table = 'military_service'
        verbose_name = 'Военный учет'
        verbose_name_plural = 'Военные учеты'
        ordering = ('created_at',)


class EducationPlace(models.Model):
    republic = models.CharField(max_length=150, blank=False, null=False,
                                verbose_name='Республика')
    region = models.CharField(max_length=150, blank=False, null=False,
                              verbose_name='Область')
    district = models.CharField(max_length=150, blank=False, null=False,
                                verbose_name='Район')
    city = models.CharField(max_length=150, blank=True, null=True,
                            verbose_name='Город')
    village = models.CharField(max_length=150, blank=True, null=True,
                               verbose_name='Село')

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')

    def __str__(self):
        return self.republic

    class Meta:
        db_table = 'education_institution'
        verbose_name = 'Данные об учебном заведении'
        verbose_name_plural = 'Данные об учебном заведении'
        ordering = ('created_at',)


class EducationType(models.Model):
    name = models.CharField(max_length=150, blank=False, null=False, verbose_name='Название')

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'education_type'
        verbose_name = 'Тип учебного заведения'
        verbose_name_plural = 'Типы учебных заведений'
        ordering = ('created_at',)


class EducationName(models.Model):
    name = models.CharField(max_length=150, blank=False, null=False, verbose_name='Название')

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'education_name'
        verbose_name = 'Учебное заведение'
        verbose_name_plural = 'Учебные заведения'
        ordering = ('created_at',)


class Education(models.Model):
    languages = (
        ('1', 'Русский'),
        ('2', 'Кыргызский'),
        ('2', 'Английский'),
        ('2', 'Немецкий'),
        ('2', 'Французский'),
    )
    original_diploma = models.BooleanField(default=False,
                                           verbose_name='Оригинал диплома/аттестата')
    excellent_student = models.BooleanField(default=False,
                                            verbose_name='Закончил на отлично')
    gold_medal = models.BooleanField(default=False,
                                     verbose_name='С золотой медалью')
    prize_winner = models.BooleanField(default=False,
                                       verbose_name='Призер олимпиад')
    diploma_or_certificate = models.BooleanField(default=False,
                                                 verbose_name='Аттестат или диплом (да - аттестат, нет - диплом')
    serial_diploma_or_certificate = models.CharField(max_length=150, blank=False, null=False,
                                                     verbose_name='Серия диплома/аттестата')
    num_diploma_or_certificate = models.CharField(max_length=150, blank=False, null=False,
                                                  verbose_name='Номер диплома/аттестата')
    year_of_issue = models.DateField(blank=False, null=False, verbose_name='Год выдачи')
    school_language = models.CharField(max_length=50, choices=languages, default='1',
                                       verbose_name='Язык обучения в школе')
    foreign_language = models.CharField(max_length=50, choices=languages, default='3',
                                        verbose_name='Иностранный язык')
    out_of_competition = models.BooleanField(default=False,
                                             verbose_name='Вне конкурса')
    kstu_student = models.BooleanField(default=False,
                                       verbose_name='Учился в этом учебном заведении')
    sport_name = models.CharField(blank=True, max_length=50, null=True, verbose_name='Вид спорта')
    sport_document_number = models.CharField(blank=True, max_length=50, null=True, verbose_name="№ документа")
    education_place = models.ForeignKey(EducationPlace, blank=False, null=False, on_delete=models.CASCADE,
                                           verbose_name='Данные об учебном заведении')
    type_of_education = models.ForeignKey(EducationType, blank=False, null=False, on_delete=models.CASCADE,
                                             verbose_name='Тип учебного заведения')
    education_name = models.ForeignKey(EducationName, blank=False, null=False, on_delete=models.CASCADE,
                                          verbose_name='Учебное заведение')
    student = models.OneToOneField(Student, blank=False, null=False, on_delete=models.CASCADE,
                                   verbose_name='Абитуриент')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')

    def __str__(self):
        return self.num_diploma_or_certificate

    class Meta:
        db_table = 'education'
        verbose_name = 'Образование'
        verbose_name_plural = 'Образования'
        ordering = ('created_at',)


class EnrollmentData(models.Model):
    education = (
        ('1', 'Бюджет'),
        ('2', 'Контракт'),
    )
    day_form = models.BooleanField(default=False,
                                   verbose_name='Дневная форма')
    language_rus = models.BooleanField(default=False,
                                       verbose_name='Язык обучения русский')
    study_form = models.CharField(max_length=50, choices=education, default='1',
                                  verbose_name='Форма контракта')
    direction = models.ForeignKey('subdivision.Direction', blank=False, null=False, on_delete=models.CASCADE,
                                  verbose_name='направление')
    recommended = models.BooleanField(default=False,
                                      verbose_name='Рекомендовать к зачислению')
    protocol = models.CharField(max_length=150, blank=True, null=True,
                                verbose_name='Протокол')
    recommended_date = models.DateField(blank=True, null=True, verbose_name='Дата рекомендации')
    paid = models.BooleanField(default=False,
                               verbose_name='Оплатил')
    confirm_enrollment = models.BooleanField(default=False,
                                             verbose_name='Подтверждение на зачисление')
    confirm_date = models.DateField(blank=True, null=True, verbose_name='Дата подтверждения')
    enrollment = models.BooleanField(default=False,
                                     verbose_name='Зачисление')
    order_num = models.CharField(max_length=150, blank=True, null=True,
                                 verbose_name='Номер приказа')
    order_date = models.DateField(blank=True, null=True, verbose_name='Дата приказа')
    protocol_num = models.CharField(max_length=150, blank=True, null=True,
                                    verbose_name='Номер протокола')
    protocol_date = models.DateField(blank=True, null=True, verbose_name='Дата протокола')
    took_docs = models.BooleanField(default=False,
                                    verbose_name='Забрал документы')
    took_docs_date = models.DateField(blank=True, null=True, verbose_name='Дата возврата документов')
    student = models.OneToOneField(Student, blank=False, null=False, on_delete=models.CASCADE,
                                   verbose_name='Абитуриент', related_name='enroll_student')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')

    def __str__(self):
        return f'{self.direction}'

    class Meta:
        db_table = 'enrollment_data'
        verbose_name = 'Данные о зачислении'
        verbose_name_plural = 'Данные о зачислении'
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
