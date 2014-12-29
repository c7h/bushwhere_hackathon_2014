# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20141220_2004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hint',
            name='place',
            field=models.ForeignKey(related_name=b'hints', to='api.Place'),
        ),
    ]
