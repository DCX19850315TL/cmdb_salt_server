# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-08-14 03:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web_models', '0002_handlelog'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostname', models.CharField(max_length=255, unique=True, verbose_name='\u4e3b\u673a\u540d')),
                ('bandwidth_limit', models.BooleanField(verbose_name='\u5e26\u5bbd\u662f\u5426\u6709\u9650\u5236')),
                ('limit_size', models.IntegerField(verbose_name='\u5e26\u5bbd\u9650\u5236\u5927\u5c0f')),
                ('room', models.CharField(blank=True, max_length=32, null=True, verbose_name='\u673a\u623f\u53f7')),
                ('cabinet_number', models.CharField(blank=True, max_length=32, null=True, verbose_name='\u673a\u67dc\u53f7')),
                ('cabinet_order', models.CharField(blank=True, max_length=32, null=True, verbose_name='\u673a\u67dc\u4e2d\u5e8f\u53f7')),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('updated_time', models.DateTimeField(auto_now=True)),
                ('memo', models.TextField(blank=True, null=True, verbose_name='\u5907\u6ce8')),
            ],
            options={
                'verbose_name': '\u8d44\u4ea7\u603b\u8868',
            },
        ),
        migrations.RenameField(
            model_name='contract',
            old_name='create_at',
            new_name='created_time',
        ),
        migrations.RenameField(
            model_name='contract',
            old_name='update_at',
            new_name='updated_time',
        ),
        migrations.RenameField(
            model_name='handlelog',
            old_name='create_at',
            new_name='created_time',
        ),
        migrations.RenameField(
            model_name='handlelog',
            old_name='update_at',
            new_name='updated_time',
        ),
        migrations.AlterField(
            model_name='deviceattribute',
            name='name',
            field=models.CharField(max_length=255, verbose_name='\u7528\u9014\u8868\u540d\u79f0'),
        ),
        migrations.AlterField(
            model_name='devicebusiness',
            name='name',
            field=models.CharField(max_length=255, verbose_name='\u4e1a\u52a1\u7ebf\u540d\u79f0'),
        ),
        migrations.AlterField(
            model_name='devicemodel',
            name='name',
            field=models.CharField(max_length=255, verbose_name='\u8bbe\u5907\u578b\u53f7\u540d\u79f0'),
        ),
        migrations.AlterField(
            model_name='devicepurpose',
            name='name',
            field=models.CharField(max_length=255, verbose_name='\u8bbe\u5907\u7528\u9014\u540d\u79f0'),
        ),
        migrations.AlterField(
            model_name='devicestatus',
            name='name',
            field=models.CharField(max_length=255, verbose_name='\u72b6\u6001\u540d\u79f0'),
        ),
        migrations.AlterField(
            model_name='devicetype',
            name='name',
            field=models.CharField(max_length=255, verbose_name='\u7c7b\u578b\u540d\u79f0'),
        ),
        migrations.AlterField(
            model_name='handlelog',
            name='handle_type',
            field=models.CharField(blank=True, max_length=255, verbose_name='\u5904\u7406\u7c7b\u578b'),
        ),
        migrations.AlterField(
            model_name='handlelog',
            name='summary',
            field=models.CharField(blank=True, max_length=255, verbose_name='\u5904\u7406\u7684\u603b\u6570'),
        ),
        migrations.AlterField(
            model_name='idcarea',
            name='name',
            field=models.CharField(max_length=255, verbose_name='\u533a\u57df\u540d\u79f0'),
        ),
        migrations.AlterField(
            model_name='networkcircuit',
            name='name',
            field=models.CharField(max_length=255, verbose_name='\u7f51\u7edc\u7ebf\u8def\u540d\u79f0'),
        ),
        migrations.AlterField(
            model_name='networktype',
            name='name',
            field=models.CharField(max_length=255, verbose_name='\u7f51\u7edc\u7c7b\u578b\u540d\u79f0'),
        ),
        migrations.AlterField(
            model_name='operatingsystem',
            name='name',
            field=models.CharField(max_length=255, verbose_name='\u64cd\u4f5c\u7cfb\u7edf\u540d\u79f0'),
        ),
        migrations.AlterField(
            model_name='permission',
            name='title',
            field=models.CharField(max_length=255, verbose_name='\u6743\u9650\u6807\u9898'),
        ),
        migrations.AlterField(
            model_name='permission',
            name='urls',
            field=models.URLField(max_length=255, verbose_name='URL\u63a7\u5236\u6743\u9650'),
        ),
        migrations.AlterField(
            model_name='role',
            name='name',
            field=models.CharField(max_length=255, verbose_name='\u89d2\u8272\u540d\u79f0'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=255, verbose_name='\u90ae\u7bb1'),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=255, verbose_name='\u5bc6\u7801'),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=255, verbose_name='\u7528\u6237\u540d'),
        ),
        migrations.AddField(
            model_name='asset',
            name='attribute',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web_models.DeviceAttribute'),
        ),
        migrations.AddField(
            model_name='asset',
            name='business',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web_models.DeviceBusiness'),
        ),
        migrations.AddField(
            model_name='asset',
            name='contract',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web_models.Contract'),
        ),
        migrations.AddField(
            model_name='asset',
            name='device_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web_models.DeviceType'),
        ),
        migrations.AddField(
            model_name='asset',
            name='idcarea',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web_models.IDCArea'),
        ),
        migrations.AddField(
            model_name='asset',
            name='network_circuit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web_models.NetworkCircuit'),
        ),
        migrations.AddField(
            model_name='asset',
            name='network_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web_models.NetworkType'),
        ),
        migrations.AddField(
            model_name='asset',
            name='operatingsystem',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web_models.OperatingSystem'),
        ),
        migrations.AddField(
            model_name='asset',
            name='purpose',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web_models.DevicePurpose'),
        ),
        migrations.AddField(
            model_name='asset',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web_models.DeviceStatus'),
        ),
        migrations.AddField(
            model_name='asset',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web_models.User'),
        ),
    ]