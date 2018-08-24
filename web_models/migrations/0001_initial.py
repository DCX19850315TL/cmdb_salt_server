# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-08-14 02:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sn', models.CharField(max_length=64, unique=True, verbose_name='\u5408\u540c\u53f7')),
                ('name', models.CharField(max_length=64, verbose_name='\u5408\u540c\u540d')),
                ('cost', models.IntegerField(verbose_name='\u5408\u540c\u91d1\u989d')),
                ('start_date', models.DateTimeField(blank=True, verbose_name='\u5408\u540c\u8d77\u59cb\u65f6\u95f4')),
                ('end_date', models.DateTimeField(blank=True, verbose_name='\u5408\u540c\u7ed3\u675f\u65f6\u95f4')),
                ('license_number', models.IntegerField(blank=True, verbose_name='license\u6570\u91cf')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('memo', models.TextField(blank=True, verbose_name='\u5907\u6ce8')),
            ],
            options={
                'verbose_name': '\u5408\u540c',
            },
        ),
        migrations.CreateModel(
            name='DeviceAttribute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='\u7528\u9014\u8868\u540d\u79f0')),
                ('memo', models.TextField(blank=True, null=True, verbose_name='\u5907\u6ce8')),
            ],
        ),
        migrations.CreateModel(
            name='DeviceBusiness',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='\u4e1a\u52a1\u7ebf\u540d\u79f0')),
                ('memo', models.TextField(blank=True, null=True, verbose_name='\u5907\u6ce8')),
            ],
        ),
        migrations.CreateModel(
            name='DeviceModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='\u8bbe\u5907\u578b\u53f7\u540d\u79f0')),
                ('memo', models.TextField(blank=True, null=True, verbose_name='\u5907\u6ce8')),
            ],
        ),
        migrations.CreateModel(
            name='DevicePurpose',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='\u8bbe\u5907\u7528\u9014\u540d\u79f0')),
                ('memo', models.TextField(blank=True, null=True, verbose_name='\u5907\u6ce8')),
            ],
        ),
        migrations.CreateModel(
            name='DeviceStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='\u72b6\u6001\u540d\u79f0')),
                ('memo', models.TextField(blank=True, null=True, verbose_name='\u5907\u6ce8')),
            ],
        ),
        migrations.CreateModel(
            name='DeviceType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='\u7c7b\u578b\u540d\u79f0')),
                ('memo', models.TextField(blank=True, null=True, verbose_name='\u5907\u6ce8')),
            ],
        ),
        migrations.CreateModel(
            name='IDCArea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='\u533a\u57df\u540d\u79f0')),
                ('memo', models.TextField(blank=True, null=True, verbose_name='\u5907\u6ce8')),
            ],
        ),
        migrations.CreateModel(
            name='NetworkCircuit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='\u7f51\u7edc\u7ebf\u8def\u540d\u79f0')),
                ('memo', models.TextField(blank=True, null=True, verbose_name='\u5907\u6ce8')),
            ],
        ),
        migrations.CreateModel(
            name='NetworkType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='\u7f51\u7edc\u7c7b\u578b\u540d\u79f0')),
                ('memo', models.TextField(blank=True, null=True, verbose_name='\u5907\u6ce8')),
            ],
        ),
        migrations.CreateModel(
            name='OperatingSystem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='\u64cd\u4f5c\u7cfb\u7edf\u540d\u79f0')),
                ('memo', models.TextField(blank=True, null=True, verbose_name='\u5907\u6ce8')),
            ],
        ),
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='\u6743\u9650\u6807\u9898')),
                ('urls', models.URLField(max_length=256, verbose_name='URL\u63a7\u5236\u6743\u9650')),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='\u66f4\u65b0\u65f6\u95f4')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
            ],
            options={
                'verbose_name': '\u6743\u9650\u8868',
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='\u89d2\u8272\u540d\u79f0')),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='\u66f4\u65b0\u65f6\u95f4')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('permissions', models.ManyToManyField(blank=True, to='web_models.Permission', verbose_name='\u5177\u6709\u7684\u6240\u6709\u6743\u9650')),
            ],
            options={
                'verbose_name': '\u89d2\u8272\u8868',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=256, verbose_name='\u7528\u6237\u540d')),
                ('password', models.CharField(max_length=256, verbose_name='\u5bc6\u7801')),
                ('is_admin', models.BooleanField(verbose_name='\u662f\u5426\u4e3a\u7ba1\u7406\u5458')),
                ('email', models.EmailField(max_length=256, verbose_name='\u90ae\u7bb1')),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='\u66f4\u65b0\u65f6\u95f4')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('roles', models.ManyToManyField(blank=True, to='web_models.Role', verbose_name='\u5177\u6709\u7684\u6240\u6709\u89d2\u8272')),
            ],
            options={
                'verbose_name': '\u7528\u6237\u8868',
            },
        ),
    ]
