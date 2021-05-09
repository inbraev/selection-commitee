# Generated by Django 3.2.2 on 2021-05-09 19:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='percs',
            options={'ordering': ('created_at',), 'verbose_name': 'Льготник', 'verbose_name_plural': 'Льготники'},
        ),
        migrations.AlterField(
            model_name='education',
            name='education_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='university.educationname', verbose_name='Учебное заведение'),
        ),
        migrations.AlterField(
            model_name='education',
            name='education_place',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='university.educationplace', verbose_name='Данные об учебном заведении'),
        ),
        migrations.AlterField(
            model_name='education',
            name='type_of_education',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='university.educationtype', verbose_name='Тип учебного заведения'),
        ),
        migrations.AlterField(
            model_name='enrollmentdata',
            name='student',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='enroll_student', to='university.student', verbose_name='Абитуриент'),
        ),
    ]
