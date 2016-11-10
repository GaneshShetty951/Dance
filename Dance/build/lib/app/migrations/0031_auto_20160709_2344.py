# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0030_auto_20160709_2342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upcomingevents',
            name='EventLink',
            field=models.URLField(default='http://www.youtube.com/'),
        ),
    ]
