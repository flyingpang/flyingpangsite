# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blogapp', '0002_auto_20150505_1611'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Classification',
        ),
    ]
