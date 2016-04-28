# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('world', '0004_auto_20160428_1741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='suittosize',
            name='created_date',
            field=models.DateField(default=datetime.datetime(2016, 4, 28, 12, 5, 29, 558900, tzinfo=utc), verbose_name='Дата добавления'),
        ),
    ]
