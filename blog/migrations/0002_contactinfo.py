# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-06 04:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FName', models.CharField(max_length=40, verbose_name='First Name:')),
                ('LName', models.CharField(max_length=40, verbose_name='Last Name:')),
                ('DoB', models.DateField(max_length=8, verbose_name='Date of Birth:')),
                ('StreetAddress', models.TextField(verbose_name='Street Address:')),
                ('City', models.TextField(verbose_name='City:')),
                ('State', models.CharField(max_length=2, verbose_name='State:')),
                ('Zipcode', models.CharField(max_length=5, verbose_name='Zipcode:')),
                ('Email', models.EmailField(max_length=254, verbose_name='Email:')),
                ('PhoneNumber', models.CharField(max_length=14, verbose_name='Phone Number:')),
            ],
        ),
    ]