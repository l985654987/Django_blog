# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-04-10 15:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20190410_1726'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
        migrations.AlterField(
            model_name='blogs',
            name='blog_type_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Blogs_type', verbose_name='博客类别'),
        ),
        migrations.AlterField(
            model_name='blogs',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.User', verbose_name='用户名'),
        ),
        migrations.AlterField(
            model_name='blogs',
            name='write_time',
            field=models.DateField(auto_now=True, verbose_name='发表时间'),
        ),
        migrations.AlterField(
            model_name='blogs_type',
            name='b_type',
            field=models.CharField(max_length=30, verbose_name='博客类别'),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=64, unique=True, verbose_name='用户名'),
        ),
    ]
