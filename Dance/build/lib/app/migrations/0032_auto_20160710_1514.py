# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0031_auto_20160709_2344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upcomingevents',
            name='EventLink',
            field=models.URLField(default='http://127.0.0.1:8000/'),
        ),
    ]
