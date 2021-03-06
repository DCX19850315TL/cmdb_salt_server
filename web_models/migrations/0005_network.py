# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-08-14 03:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web_models', '0004_server'),
    ]

    operations = [
        migrations.CreateModel(
            name='Network',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('port_number', models.IntegerField(verbose_name='\u7aef\u53e3\u6570\u91cf')),
                ('capacity', models.IntegerField(verbose_name='\u541e\u5410\u80fd\u529b')),
                ('sn', models.CharField(max_length=64, verbose_name='SN\u53f7')),
                ('manufactory', models.CharField(blank=True, max_length=64, null=True, verbose_name='\u5236\u9020\u5546')),
                ('model', models.CharField(blank=True, max_length=128, null=True, verbose_name='\u578b\u53f7')),
                ('asset_number', models.CharField(max_length=64, verbose_name='\u8d44\u4ea7\u7f16\u53f7')),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('updated_time', models.DateTimeField(auto_now=True)),
                ('memo', models.TextField(blank=True, verbose_name='\u5907\u6ce8')),
                ('asset', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='web_models.Asset')),
            ],
            options={
                'verbose_name': '\u7f51\u7edc\u8bbe\u5907',
            },
        ),
    ]
