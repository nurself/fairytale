# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('passport_data', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=50)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Suit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('picture', models.CharField(max_length=100, blank=True, null=True)),
                ('vendor_code', models.CharField(max_length=10)),
                ('year_issue', models.IntegerField()),
                ('details', models.TextField(max_length=100)),
                ('colour', models.CharField(max_length=50)),
                ('rent_price', models.IntegerField()),
                ('item_price', models.IntegerField()),
                ('note', models.TextField(max_length=50)),
                ('branch', models.ForeignKey(to='world.Branch')),
            ],
        ),
        migrations.CreateModel(
            name='SuitToRent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('count', models.IntegerField()),
                ('start_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('end_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('total_price', models.IntegerField()),
                ('published_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('people', models.ForeignKey(to='world.People')),
            ],
        ),
        migrations.CreateModel(
            name='SuitToSize',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('size', models.IntegerField()),
                ('count', models.IntegerField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('suit', models.ForeignKey(to='world.Suit')),
            ],
        ),
        migrations.CreateModel(
            name='UserToBranch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('branch', models.ForeignKey(to='world.Branch')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='suittorent',
            name='suit_to_size',
            field=models.ForeignKey(to='world.SuitToSize'),
        ),
        migrations.AddField(
            model_name='suittorent',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
