# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-03 08:57
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0007_alter_validators_add_error_messages'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='Email адрес')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активный')),
                ('is_admin', models.BooleanField(default=False, verbose_name='Администратор')),
                ('is_staff', models.BooleanField(default=True, verbose_name='Персонал')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
        ),
        migrations.CreateModel(
            name='Agreement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('protocol_num', models.CharField(max_length=20, verbose_name='Номер договора')),
                ('start_date', models.DateField(default=django.utils.timezone.now, verbose_name='Дата начала проката')),
                ('end_date', models.DateField(default=django.utils.timezone.now, verbose_name='Дата конца проката')),
                ('reserve_sum', models.IntegerField(verbose_name='Сумма при брони')),
                ('total_price', models.IntegerField(verbose_name='Общая сумма')),
                ('published_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата записи')),
                ('is_returned', models.NullBooleanField(verbose_name='Возвращено?')),
            ],
            options={
                'verbose_name': 'Договор',
                'verbose_name_plural': 'База договоров',
            },
        ),
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Наименование')),
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
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='ФИО')),
                ('passport_data', models.CharField(blank=True, max_length=50, null=True, verbose_name='Паспортные данные')),
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
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Наименование')),
                ('picture', models.ImageField(blank=True, null=True, upload_to='images', verbose_name='Картинка')),
                ('vendor_code', models.CharField(max_length=10, verbose_name='Артикул')),
                ('year_issue', models.IntegerField(verbose_name='Год производства')),
                ('details', models.TextField(max_length=100, verbose_name='Детализация')),
                ('colour', models.CharField(max_length=50, verbose_name='Цвет')),
                ('rent_price', models.IntegerField(verbose_name='Арендная плата')),
                ('item_price', models.IntegerField(verbose_name='Сумма имущества')),
                ('note', models.CharField(blank=True, max_length=50, null=True, verbose_name='Примечание')),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='world.Branch', verbose_name='Филиал')),
            ],
            options={
                'verbose_name': 'Инвентарь',
                'verbose_name_plural': 'Инвентаризация',
            },
        ),
        migrations.CreateModel(
            name='SuitToRent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(verbose_name='Количество')),
                ('agreement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='world.Agreement', verbose_name='Номер договора')),
            ],
            options={
                'verbose_name': 'Инвентарь',
                'verbose_name_plural': 'Комплект',
            },
        ),
        migrations.CreateModel(
            name='SuitToSize',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.IntegerField(verbose_name='Размер')),
                ('count', models.IntegerField(verbose_name='Количество')),
                ('created_date', models.DateField(default=datetime.datetime(2016, 5, 3, 8, 57, 24, 487000, tzinfo=utc), verbose_name='Дата добавления')),
                ('suit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='world.Suit', verbose_name='Инвентарь')),
            ],
            options={
                'verbose_name': 'Размер',
                'verbose_name_plural': 'Размеры инвентарей',
            },
        ),
        migrations.CreateModel(
            name='SuitType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Наименование')),
            ],
            options={
                'verbose_name': 'Отдел',
                'verbose_name_plural': 'Отделы',
            },
        ),
        migrations.CreateModel(
            name='SystemErrorLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(max_length=200)),
                ('message', models.TextField()),
                ('timestamp', models.DateTimeField(blank=True, null=True, verbose_name='Дата и время')),
            ],
        ),
        migrations.AddField(
            model_name='suittorent',
            name='suit_to_size',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='world.SuitToSize', verbose_name='Инвентарь'),
        ),
        migrations.AddField(
            model_name='suit',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='world.SuitType', verbose_name='Отдел'),
        ),
        migrations.AddField(
            model_name='agreement',
            name='people',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='world.People', verbose_name='Наниматель'),
        ),
        migrations.AddField(
            model_name='agreement',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Наймодатель'),
        ),
        migrations.AddField(
            model_name='myuser',
            name='branch',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='world.Branch', verbose_name='Филиал'),
        ),
        migrations.AddField(
            model_name='myuser',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='myuser',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
        migrations.AlterUniqueTogether(
            name='suittosize',
            unique_together=set([('suit', 'size')]),
        ),
        migrations.AlterUniqueTogether(
            name='suittorent',
            unique_together=set([('agreement', 'suit_to_size')]),
        ),
    ]
