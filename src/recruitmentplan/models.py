from django.db import models
from src.subdivision.models import Faculty, Direction, Section
from src.subdivision.services import form_education, education


class Plan(models.Model):
    faculty = models.ForeignKey(Faculty, blank=False, null=False, on_delete=models.CASCADE, verbose_name='факультет')
    direction = models.ForeignKey(Direction, blank=False, null=False, on_delete=models.CASCADE,
                                  verbose_name='направление')
    section = models.ForeignKey(Section, blank=False, null=False, on_delete=models.CASCADE, verbose_name='профиль')
    form_education = models.CharField(max_length=50, choices=form_education, default=form_education[0][1],
                                      verbose_name='форма обучение')
    education = models.CharField(max_length=50, choices=education, default='1', verbose_name='обучение')
    additional_item = models.PositiveSmallIntegerField(default=0, blank=False, null=False,
                                                       verbose_name='кол-во дополнительных предметов')
    planned_place = models.PositiveSmallIntegerField(default=0, blank=False, null=False,
                                                     verbose_name='кол-во плановых мест')
    doc_money = models.FloatField(default=0.0, blank=False, null=False, verbose_name='сумма за прием документов')
    study_money = models.FloatField(default=0.0, blank=False, null=False, verbose_name='сумма за обучение')
    req_additional_subject = models.BooleanField(default=False,
                                                 verbose_name='обязательный дополнительные предметные тесты')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')

    def __str__(self):
        return f'{self.faculty}'

    class Meta:
        db_table = 'plan'
        verbose_name = 'План'
        verbose_name_plural = 'Планы'
        ordering = ('created_at',)


class OrtScore(models.Model):
    plan = models.OneToOneField(Plan, blank=False, null=False, on_delete=models.CASCADE, verbose_name='план набора')
    basic_score = models.PositiveSmallIntegerField(default=0, blank=False, null=False, verbose_name='основной балл')
    kyr_sub_score = models.PositiveSmallIntegerField(default=0, blank=False, null=False, verbose_name='кыргызский язык')
    bio_sub_score = models.PositiveSmallIntegerField(default=0, blank=False, null=False, verbose_name='биология')
    phy_sub_score = models.PositiveSmallIntegerField(default=0, blank=False, null=False, verbose_name='физика')
    chem_sub_score = models.PositiveSmallIntegerField(default=0, blank=False, null=False, verbose_name='химия')
    math_sub_score = models.PositiveSmallIntegerField(default=0, blank=False, null=False, verbose_name='математика')
    his_sub_score = models.PositiveSmallIntegerField(default=0, blank=False, null=False, verbose_name='история')
    eng_sub_score = models.PositiveSmallIntegerField(default=0, blank=False, null=False, verbose_name='англиский язык')
    rus_sub_score = models.PositiveSmallIntegerField(default=0, blank=False, null=False, verbose_name='русский язык')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')

    def __str__(self):
        return f'{self.basic_score}'

    class Meta:
        db_table = 'ort_score'
        verbose_name = 'Орт балл'
        verbose_name_plural = 'Орт баллы'
        ordering = ('created_at',)