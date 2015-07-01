# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blogapp', '0004_auto_20150505_1849'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='author',
            field=models.ForeignKey(related_query_name=b'article', related_name='articles', to='Blogapp.Author'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='article',
            name='classification',
            field=models.CharField(max_length=20, null=True, verbose_name='type', choices=[(b'Django', 'Django'), (b'Linux', 'Linux'), (b'Python', 'Python'), (b'CSS', 'CSS'), (b'Other', 'Other')]),
            preserve_default=True,
        ),
    ]
