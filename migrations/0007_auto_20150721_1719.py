# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workflow', '0006_auto_20150721_1255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='state',
            field=models.CharField(default=b'1', max_length=5, verbose_name='\u72b6\u6001', choices=[(b'0', b'\xe5\xb7\xb2\xe6\x8b\x92\xe7\xbb\x9d'), (b'1', b'\xe6\x96\xb0\xe5\xbb\xba\xe4\xb8\xad'), (b'2', b'\xe5\xb7\xb2\xe6\x8f\x90\xe4\xba\xa4'), (b'3', b'\xe5\xb7\xb2\xe5\xae\xa1\xe6\x89\xb9'), (b'4', b'\xe5\xb7\xb2\xe5\xa4\x84\xe7\x90\x86'), (b'5', b'\xe5\xb7\xb2\xe7\xa1\xae\xe8\xae\xa4'), (b'6', b'\xe5\xb7\xb2\xe5\xae\x8c\xe6\x88\x90')]),
        ),
    ]
