# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_auto_20141127_0309'),
    ]

    operations = [
        migrations.AddField(
            model_name='movies',
            name='fun_facts',
            field=models.CharField(default=b'', max_length=256),
            preserve_default=True,
        ),
    ]
