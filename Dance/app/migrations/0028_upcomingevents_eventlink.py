# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0027_auto_20160708_2058'),
    ]

    operations = [
        migrations.AddField(
            model_name='upcomingevents',
            name='EventLink',
            field=models.URLField(default='www.youtube.com'),
        ),
    ]
