# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(verbose_name='last login', null=True, blank=True)),
                ('email', models.EmailField(unique=True, max_length=255, verbose_name='email address')),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=50, verbose_name='Наименование')),
                ('address', models.CharField(max_length=50, verbose_name='Адрес')),
            ],
            options={
                'verbose_name': 'Филиал',
                'verbose_name_plural': 'Филиалы',
            },
        ),
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=100, verbose_name='ФИО')),
                ('passport_data', models.CharField(max_length=50, verbose_name='Паспортные данные', null=True, blank=True)),
                ('address', models.CharField(max_length=100, verbose_name='Адрес проживания')),
                ('phone', models.CharField(max_length=50, verbose_name='Телефон')),
            ],
            options={
                'verbose_name': 'Наниматель',
                'verbose_name_plural': 'База нанимателей',
            },
        ),
        migrations.CreateModel(
            name='Suit',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=100, verbose_name='Наименование')),
                ('picture', models.ImageField(upload_to='images', verbose_name='Картинка', null=True, blank=True)),
                ('vendor_code', models.CharField(max_length=10, verbose_name='Артикул')),
                ('year_issue', models.IntegerField(verbose_name='Год производства')),
                ('details', models.TextField(max_length=100, verbose_name='Детализация')),
                ('colour', models.CharField(max_length=50, verbose_name='Цвет')),
                ('rent_price', models.IntegerField(verbose_name='Арендная плата')),
                ('item_price', models.IntegerField(verbose_name='Сумма имущества')),
                ('note', models.CharField(max_length=50, verbose_name='Примечание', null=True, blank=True)),
                ('branch', models.ForeignKey(verbose_name='Филиал', to='world.Branch')),
            ],
            options={
                'verbose_name': 'Инвентарь',
                'verbose_name_plural': 'Инвентаризация',
            },
        ),
        migrations.CreateModel(
            name='SuitToRent',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('protocol_num', models.CharField(max_length=20, verbose_name='Номер договора')),
                ('count', models.IntegerField(verbose_name='Количество')),
                ('start_date', models.DateField(default=django.utils.timezone.now, verbose_name='Дата начала проката')),
                ('end_date', models.DateField(default=django.utils.timezone.now, verbose_name='Дата конца проката')),
                ('reserve_sum', models.IntegerField(verbose_name='Сумма при брони')),
                ('total_price', models.IntegerField(verbose_name='Общая сумма')),
                ('published_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата записи')),
                ('is_returned', models.NullBooleanField(verbose_name='Возвращено?')),
                ('people', models.ForeignKey(verbose_name='Наниматель', to='world.People')),
            ],
            options={
                'verbose_name': 'Договор',
                'verbose_name_plural': 'База договоров',
            },
        ),
        migrations.CreateModel(
            name='SuitToSize',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('size', models.IntegerField(default=1, verbose_name='Размер')),
                ('count', models.IntegerField(default=1, verbose_name='Количество')),
                ('created_date', models.DateField(verbose_name='Дата добавления')),
                ('suit', models.ForeignKey(verbose_name='Инвентарь', to='world.Suit')),
            ],
            options={
                'verbose_name_plural': 'Размеры инвентарей',
                'verbose_name': 'Размер',
            },
        ),
        migrations.CreateModel(
            name='SuitType',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=50, verbose_name='Наименование')),
            ],
            options={
                'verbose_name': 'Отдел',
                'verbose_name_plural': 'Отделы',
            },
        ),
        migrations.AddField(
            model_name='suittorent',
            name='suit_to_size',
            field=models.ForeignKey(verbose_name='Инвентарь', to='world.SuitToSize'),
        ),
        migrations.AddField(
            model_name='suittorent',
            name='user',
            field=models.ForeignKey(verbose_name='Наймодатель', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='suit',
            name='type',
            field=models.ForeignKey(verbose_name='Отдел', to='world.SuitType'),
        ),
        migrations.AddField(
            model_name='myuser',
            name='branch',
            field=models.ForeignKey(null=True, to='world.Branch', blank=True),
        ),
        migrations.AlterUniqueTogether(
            name='suittosize',
            unique_together=set([('suit', 'size')]),
        ),
    ]
