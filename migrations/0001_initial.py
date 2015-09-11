# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=30, verbose_name='\u6807\u9898')),
                ('description', models.TextField(verbose_name='\u63cf\u8ff0')),
                ('state', models.CharField(max_length=5, choices=[(b'1', b'\xe6\x96\xb0\xe5\xbb\xba\xe4\xb8\xad'), (b'2', b'\xe5\xae\xa1\xe6\x89\xb9\xe4\xb8\xad'), (b'3', b'\xe5\xa4\x84\xe7\x90\x86\xe4\xb8\xad'), (b'4', b'\xe5\xb7\xb2\xe5\xae\x8c\xe6\x88\x90')])),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('expire_Time', models.DateTimeField(verbose_name='\u671f\u671b\u65f6\u95f4')),
                ('finish_time', models.DateTimeField(auto_now=True, verbose_name='\u5b8c\u6210\u65f6\u95f4')),
                ('creator', models.ForeignKey(verbose_name='\u521b\u5efa\u4eba', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-create_time'],
                'verbose_name': '\u4efb\u52a1\u521b\u5efa',
                'verbose_name_plural': '\u4efb\u52a1\u521b\u5efa',
            },
        ),
        migrations.CreateModel(
            name='Workorder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=30, verbose_name='\u6807\u9898')),
                ('description', models.TextField(verbose_name='\u63cf\u8ff0', blank=True)),
                ('take_time', models.IntegerField(verbose_name='\u8017\u8d39\u65f6\u95f4')),
                ('auditor', models.ManyToManyField(related_name='workorder_auditor', verbose_name='\u5ba1\u6279\u4eba', to=settings.AUTH_USER_MODEL)),
                ('creator', models.ForeignKey(verbose_name='\u521b\u5efa\u4eba', to=settings.AUTH_USER_MODEL)),
                ('operator', models.ManyToManyField(related_name='workorder_operator', verbose_name='\u6267\u884c\u4eba', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['id'],
                'verbose_name': '\u6807\u51c6\u5de5\u5355',
                'verbose_name_plural': '\u6807\u51c6\u5de5\u5355',
            },
        ),
        migrations.AddField(
            model_name='task',
            name='type',
            field=models.ForeignKey(verbose_name='\u4efb\u52a1\u7c7b\u578b', to='workflow.Workorder'),
        ),
    ]
