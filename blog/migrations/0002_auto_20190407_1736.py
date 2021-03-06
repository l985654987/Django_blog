# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-04-07 09:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blogs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_title', models.CharField(max_length=100)),
                ('blog_matter', models.TextField()),
                ('write_time', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Blogs_type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('b_type', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='blogs',
            name='blog_type_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Blogs_type'),
        ),
        migrations.AddField(
            model_name='blogs',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.User'),
        ),
    ]
