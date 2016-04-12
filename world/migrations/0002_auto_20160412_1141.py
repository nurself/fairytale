# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('world', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='branch',
            options={'verbose_name': 'Филиал', 'verbose_name_plural': 'Филиалы'},
        ),
        migrations.AlterModelOptions(
            name='suit',
            options={'verbose_name': 'Костюм', 'verbose_name_plural': 'Костюмы'},
        ),
        migrations.AlterField(
            model_name='branch',
            name='address',
            field=models.CharField(verbose_name='Адрес', max_length=50),
        ),
        migrations.AlterField(
            model_name='branch',
            name='name',
            field=models.CharField(verbose_name='Наименование', max_length=50),
        ),
        migrations.AlterField(
            model_name='people',
            name='address',
            field=models.CharField(verbose_name='Адрес проживания', max_length=100),
        ),
        migrations.AlterField(
            model_name='people',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата добавления'),
        ),
        migrations.AlterField(
            model_name='people',
            name='name',
            field=models.CharField(verbose_name='ФИО', max_length=100),
        ),
        migrations.AlterField(
            model_name='people',
            name='passport_data',
            field=models.CharField(verbose_name='Паспортные данные', max_length=50),
        ),
        migrations.AlterField(
            model_name='people',
            name='phone',
            field=models.CharField(verbose_name='Телефон', max_length=50),
        ),
        migrations.AlterField(
            model_name='suit',
            name='branch',
            field=models.ForeignKey(verbose_name='Филиал', to='world.Branch'),
        ),
        migrations.AlterField(
            model_name='suit',
            name='colour',
            field=models.CharField(verbose_name='Цвет', max_length=50),
        ),
        migrations.AlterField(
            model_name='suit',
            name='details',
            field=models.TextField(verbose_name='Детализация', max_length=100),
        ),
        migrations.AlterField(
            model_name='suit',
            name='item_price',
            field=models.IntegerField(verbose_name='Сумма имущества'),
        ),
        migrations.AlterField(
            model_name='suit',
            name='name',
            field=models.CharField(verbose_name='Наименование', max_length=100),
        ),
        migrations.AlterField(
            model_name='suit',
            name='note',
            field=models.CharField(blank=True, verbose_name='Примечание', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='suit',
            name='picture',
            field=models.FileField(blank=True, verbose_name='Картинка', upload_to='files', null=True),
        ),
        migrations.AlterField(
            model_name='suit',
            name='rent_price',
            field=models.IntegerField(verbose_name='Арендная плата'),
        ),
        migrations.AlterField(
            model_name='suit',
            name='vendor_code',
            field=models.CharField(verbose_name='Артикул', max_length=10),
        ),
        migrations.AlterField(
            model_name='suit',
            name='year_issue',
            field=models.IntegerField(verbose_name='Год производства'),
        ),
    ]
