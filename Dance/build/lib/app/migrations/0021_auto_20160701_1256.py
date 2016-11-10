# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0020_auto_20160620_2113'),
    ]

    operations = [
        migrations.AddField(
            model_name='upcomingevents',
            name='EventType',
            field=models.CharField(default='drama', max_length=100),
        ),
        migrations.AddField(
            model_name='upcomingevents',
            name='ShowCategory',
            field=models.CharField(default='ticketed', max_length=100),
        ),
    ]
