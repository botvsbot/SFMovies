# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_movies_fun_facts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='fun_facts',
            field=models.CharField(default=b'', max_length=512),
            preserve_default=True,
        ),
    ]
