# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('world', '0006_auto_20160412_1729'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='suittosize',
            options={'verbose_name_plural': 'Размеры инвентарей', 'verbose_name': 'Размер'},
        ),
        migrations.AlterField(
            model_name='branch',
            name='name',
            field=models.CharField(verbose_name='Наименование', unique=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='people',
            name='name',
            field=models.CharField(verbose_name='ФИО', unique=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='suit',
            name='name',
            field=models.CharField(verbose_name='Наименование', unique=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='suittosize',
            name='count',
            field=models.IntegerField(verbose_name='Количество', default=1),
        ),
        migrations.AlterField(
            model_name='suittosize',
            name='size',
            field=models.IntegerField(verbose_name='Размер', default=1),
        ),
    ]
