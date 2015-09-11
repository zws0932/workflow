# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workflow', '0004_auto_20150721_1248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='state',
            field=models.CharField(default=1, max_length=5, verbose_name='\u72b6\u6001', choices=[(0, b'\xe5\xb7\xb2\xe6\x8b\x92\xe7\xbb\x9d'), (1, b'\xe6\x96\xb0\xe5\xbb\xba\xe4\xb8\xad'), (2, b'\xe5\xb7\xb2\xe6\x8f\x90\xe4\xba\xa4'), (3, b'\xe5\xbe\x85\xe5\xae\xa1\xe6\x89\xb9'), (4, b'\xe5\xb7\xb2\xe5\xae\xa1\xe6\x89\xb9'), (5, b'\xe5\xbe\x85\xe5\xa4\x84\xe7\x90\x86'), (6, b'\xe5\xb7\xb2\xe5\xa4\x84\xe7\x90\x86'), (7, b'\xe5\xb7\xb2\xe7\xa1\xae\xe8\xae\xa4'), (8, b'\xe5\xb7\xb2\xe5\xae\x8c\xe6\x88\x90')]),
        ),
    ]
