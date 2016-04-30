# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('world', '0006_auto_20160429_1639'),
    ]

    operations = [
        migrations.CreateModel(
            name='SystemErrorLog',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(max_length=200)),
                ('message', models.TextField()),
                ('timestamp', models.DateTimeField(null=True, blank=True, verbose_name='Дата и время')),
            ],
        ),
        migrations.AlterModelOptions(
            name='suittorent',
            options={'verbose_name_plural': 'Комплект', 'verbose_name': 'Инвентарь'},
        ),
        migrations.AlterField(
            model_name='myuser',
            name='branch',
            field=models.ForeignKey(to='world.Branch', blank=True, null=True, verbose_name='Филиал'),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='email',
            field=models.EmailField(max_length=255, unique=True, verbose_name='Email адрес'),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Активный'),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='is_admin',
            field=models.BooleanField(default=False, verbose_name='Администратор'),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='is_staff',
            field=models.BooleanField(default=True, verbose_name='Персонал'),
        ),
        migrations.AlterField(
            model_name='suittosize',
            name='created_date',
            field=models.DateField(default=datetime.datetime(2016, 4, 30, 5, 56, 3, 849000, tzinfo=utc), verbose_name='Дата добавления'),
        ),
        migrations.AlterUniqueTogether(
            name='suittorent',
            unique_together=set([('agreement', 'suit_to_size')]),
        ),
    ]
