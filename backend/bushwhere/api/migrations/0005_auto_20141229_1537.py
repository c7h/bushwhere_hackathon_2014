# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20141229_1031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='image',
            field=models.ImageField(upload_to=b'profilepictures'),
        ),
    ]
