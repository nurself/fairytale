# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('world', '0003_auto_20160428_1740'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='is_staff',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='suittosize',
            name='created_date',
            field=models.DateField(verbose_name='Дата добавления', default=datetime.datetime(2016, 4, 28, 11, 41, 25, 633400, tzinfo=utc)),
        ),
    ]
