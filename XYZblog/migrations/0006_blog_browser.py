# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-02 09:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('XYZblog', '0005_blog_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='browser',
            field=models.IntegerField(default=0, verbose_name='浏览量'),
            preserve_default=False,
        ),
    ]
