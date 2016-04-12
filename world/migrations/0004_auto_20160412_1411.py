# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('world', '0003_auto_20160412_1147'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='people',
            options={'verbose_name': 'Наниматель', 'verbose_name_plural': 'База нанимателей'},
        ),
        migrations.AlterModelOptions(
            name='suit',
            options={'verbose_name': 'Инвентарь', 'verbose_name_plural': 'Инвентаризация'},
        ),
        migrations.AlterModelOptions(
            name='suittorent',
            options={'verbose_name': 'Договор', 'verbose_name_plural': 'База договоров'},
        ),
        migrations.RemoveField(
            model_name='people',
            name='created_date',
        ),
        migrations.AddField(
            model_name='suittorent',
            name='protocol_num',
            field=models.CharField(verbose_name='Номер договора', max_length=20, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='suittorent',
            name='count',
            field=models.IntegerField(verbose_name='Количество'),
        ),
        migrations.AlterField(
            model_name='suittorent',
            name='end_date',
            field=models.DateTimeField(verbose_name='Дата конца проката', default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='suittorent',
            name='people',
            field=models.ForeignKey(verbose_name='Наниматель', to='world.People'),
        ),
        migrations.AlterField(
            model_name='suittorent',
            name='published_date',
            field=models.DateTimeField(verbose_name='Дата записи', default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='suittorent',
            name='start_date',
            field=models.DateTimeField(verbose_name='Дата начала проката', default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='suittorent',
            name='suit_to_size',
            field=models.ForeignKey(verbose_name='Инвентарь', to='world.SuitToSize'),
        ),
        migrations.AlterField(
            model_name='suittorent',
            name='total_price',
            field=models.IntegerField(verbose_name='Общая сумма'),
        ),
        migrations.AlterField(
            model_name='suittorent',
            name='user',
            field=models.ForeignKey(verbose_name='Наймодатель', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='suittosize',
            name='count',
            field=models.IntegerField(verbose_name='Количество'),
        ),
        migrations.AlterField(
            model_name='suittosize',
            name='created_date',
            field=models.DateTimeField(verbose_name='Дата добавления', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='suittosize',
            name='size',
            field=models.IntegerField(verbose_name='Размер'),
        ),
        migrations.AlterField(
            model_name='suittosize',
            name='suit',
            field=models.ForeignKey(verbose_name='Инвентарь', to='world.Suit'),
        ),
    ]
