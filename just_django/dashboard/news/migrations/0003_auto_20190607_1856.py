# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-06-07 18:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20190607_0943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='headline',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
