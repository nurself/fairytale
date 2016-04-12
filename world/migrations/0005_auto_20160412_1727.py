# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('world', '0004_auto_20160412_1411'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='suittosize',
            options={'verbose_name': 'Размер', 'verbose_name_plural': 'Размеры'},
        ),
        migrations.AlterField(
            model_name='suit',
            name='picture',
            field=models.ImageField(upload_to='images', verbose_name='Картинка', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='suittosize',
            name='created_date',
            field=models.DateField(verbose_name='Дата добавления', blank=True, null=True),
        ),
    ]
