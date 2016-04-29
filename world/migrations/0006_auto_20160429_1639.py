# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import datetime
from django.utils.timezone import utc
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('world', '0005_auto_20160428_1805'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agreement',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('protocol_num', models.CharField(max_length=20, verbose_name='Номер договора')),
                ('start_date', models.DateField(default=django.utils.timezone.now, verbose_name='Дата начала проката')),
                ('end_date', models.DateField(default=django.utils.timezone.now, verbose_name='Дата конца проката')),
                ('reserve_sum', models.IntegerField(verbose_name='Сумма при брони')),
                ('total_price', models.IntegerField(verbose_name='Общая сумма')),
                ('published_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата записи')),
                ('is_returned', models.NullBooleanField(verbose_name='Возвращено?')),
                ('people', models.ForeignKey(verbose_name='Наниматель', to='world.People')),
                ('user', models.ForeignKey(verbose_name='Наймодатель', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'База договоров',
                'verbose_name': 'Договор',
            },
        ),
        migrations.AlterModelOptions(
            name='suittorent',
            options={},
        ),
        migrations.RemoveField(
            model_name='suittorent',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='suittorent',
            name='is_returned',
        ),
        migrations.RemoveField(
            model_name='suittorent',
            name='people',
        ),
        migrations.RemoveField(
            model_name='suittorent',
            name='protocol_num',
        ),
        migrations.RemoveField(
            model_name='suittorent',
            name='published_date',
        ),
        migrations.RemoveField(
            model_name='suittorent',
            name='reserve_sum',
        ),
        migrations.RemoveField(
            model_name='suittorent',
            name='start_date',
        ),
        migrations.RemoveField(
            model_name='suittorent',
            name='total_price',
        ),
        migrations.RemoveField(
            model_name='suittorent',
            name='user',
        ),
        migrations.AlterField(
            model_name='suittosize',
            name='created_date',
            field=models.DateField(default=datetime.datetime(2016, 4, 29, 10, 39, 0, 685000, tzinfo=utc), verbose_name='Дата добавления'),
        ),
        migrations.AddField(
            model_name='suittorent',
            name='agreement',
            field=models.ForeignKey(to='world.Agreement', blank=True, verbose_name='Номер договора', null=True),
        ),
    ]
