# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blogapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='classification',
            field=models.CharField(max_length=20, null=True, verbose_name='type', choices=[(b'A', 'django'), (b'B', 'linux'), (b'C', 'python'), (b'D', 'CSS')]),
            preserve_default=True,
        ),
    ]
