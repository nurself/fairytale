# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('world', '0002_auto_20160412_1141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='suit',
            name='picture',
            field=models.ImageField(upload_to='files', blank=True, verbose_name='Картинка', null=True),
        ),
    ]
