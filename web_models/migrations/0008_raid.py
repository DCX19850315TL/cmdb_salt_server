# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-08-14 03:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web_models', '0007_memory'),
    ]

    operations = [
        migrations.CreateModel(
            name='Raid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=255, verbose_name='Raid\u578b\u53f7')),
                ('is_onboard', models.BooleanField(verbose_name='\u662f\u5426\u677f\u8f7d')),
                ('raid_group', models.IntegerField(verbose_name='Raid\u662f0\uff0c1\uff0c5\u8fd8\u662f10')),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('updated_time', models.DateTimeField(auto_now=True)),
                ('memo', models.TextField(blank=True, verbose_name='\u5907\u6ce8')),
                ('server_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web_models.Server')),
            ],
            options={
                'verbose_name': 'RAID',
            },
        ),
    ]
