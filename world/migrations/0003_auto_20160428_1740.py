# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('world', '0002_auto_20160428_1730'),
    ]

    operations = [
        migrations.AlterField(
            model_name='suittosize',
            name='created_date',
            field=models.DateField(default=datetime.datetime(2016, 4, 28, 11, 40, 15, 153400, tzinfo=utc), verbose_name='Дата добавления'),
        ),
    ]
