# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('movie_id', models.IntegerField(default=0, unique=True)),
                ('title', models.CharField(max_length=128)),
                ('release_year', models.IntegerField(default=0)),
                ('location_id', models.CharField(max_length=128)),
                ('producer', models.CharField(max_length=128)),
                ('director', models.CharField(max_length=128)),
                ('distributor', models.CharField(max_length=128)),
                ('actor1', models.CharField(max_length=128)),
                ('actor2', models.CharField(max_length=128)),
                ('actor3', models.CharField(max_length=128)),
                ('lat', models.DecimalField(default=0.0, max_digits=50, decimal_places=40)),
                ('lng', models.DecimalField(default=0.0, max_digits=50, decimal_places=40)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
