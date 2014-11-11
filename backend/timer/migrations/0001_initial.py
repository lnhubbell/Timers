# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Timer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('seconds', models.PositiveIntegerField(default=0, verbose_name=b'Time in Seconds')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
