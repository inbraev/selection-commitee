# Generated by Django 3.2.2 on 2021-05-09 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_permissioncommissioner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='permissioncommissioner',
            name='education',
            field=models.CharField(choices=[('1', 'Бюджет'), ('2', 'Контракт')], default='1', max_length=50, verbose_name='обучение'),
        ),
    ]