# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('world', '0005_auto_20160412_1727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='suittorent',
            name='end_date',
            field=models.DateField(verbose_name='Дата конца проката', default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='suittorent',
            name='start_date',
            field=models.DateField(verbose_name='Дата начала проката', default=django.utils.timezone.now),
        ),
    ]
