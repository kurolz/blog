# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
# import ckeditor.fields

class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(verbose_name='标题', max_length=32)),
                ('author', models.CharField(verbose_name='作者', max_length=16)),
                ('content', models.TextField(verbose_name='正文', blank=True, null=True)),
                ('created', models.DateTimeField(verbose_name='发布时间', auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(verbose_name='名称', max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(verbose_name='称呼', max_length=16)),
                ('email', models.EmailField(verbose_name='邮箱', max_length=254)),
                ('content', models.CharField(verbose_name='内容', max_length=140)),
                ('created', models.DateTimeField(verbose_name='发布时间', auto_now_add=True)),
                ('blog', models.ForeignKey(verbose_name='博客', to='XYZblog.Blog')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(verbose_name='名称', max_length=16)),
            ],
        ),
        migrations.AddField(
            model_name='blog',
            name='category',
            field=models.ForeignKey(verbose_name='分类', to='XYZblog.Category'),
        ),
        migrations.AddField(
            model_name='blog',
            name='tags',
            field=models.ManyToManyField(verbose_name='标签', to='XYZblog.Tag'),
        ),
    ]
