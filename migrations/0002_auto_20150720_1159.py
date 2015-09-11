# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workflow', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='expire_Time',
            new_name='expire_time',
        ),
        migrations.AlterField(
            model_name='workorder',
            name='take_time',
            field=models.IntegerField(verbose_name='\u9700\u8981\u65f6\u95f4'),
        ),
    ]
