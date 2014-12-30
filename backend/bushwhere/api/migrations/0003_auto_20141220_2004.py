# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0002_auto_20141215_1622'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='last_login',
        ),
        migrations.RemoveField(
            model_name='player',
            name='name',
        ),
        migrations.RemoveField(
            model_name='player',
            name='password',
        ),
        migrations.AddField(
            model_name='player',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
