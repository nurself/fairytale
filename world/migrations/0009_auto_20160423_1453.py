# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('world', '0008_suittorent_is_returned'),
    ]

    operations = [
        migrations.CreateModel(
            name='SuitType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.CharField(unique=True, verbose_name='Наименование', max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Отделы',
                'verbose_name': 'Отдел',
            },
        ),
        migrations.AddField(
            model_name='suittorent',
            name='reserve_sum',
            field=models.IntegerField(verbose_name='Сумма при брони', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='people',
            name='passport_data',
            field=models.CharField(verbose_name='Паспортные данные', null=True, blank=True, max_length=50),
        ),
        migrations.AlterUniqueTogether(
            name='suittosize',
            unique_together=set([('suit', 'size')]),
        ),
        migrations.AddField(
            model_name='suit',
            name='type',
            field=models.ForeignKey(null=True, to='world.SuitType', blank=True, verbose_name='Отдел'),
        ),
    ]
