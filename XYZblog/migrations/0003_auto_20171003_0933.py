# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-10-03 01:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('XYZblog', '0002_auto_20171003_0917'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='browser',
            field=models.IntegerField(default=0, editable=False, verbose_name='浏览量'),
        ),
    ]
