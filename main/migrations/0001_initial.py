# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-04-26 00:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Box',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('box_id', models.CharField(max_length=200)),
                ('box_label', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=200)),
                ('item_description', models.CharField(max_length=200)),
                ('votes', models.IntegerField(default=0)),
                ('box', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Box')),
            ],
        ),
    ]
