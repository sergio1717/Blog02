# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-03 09:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog02', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='category',
            field=models.ManyToManyField(to='Blog02.Post'),
        ),
    ]
