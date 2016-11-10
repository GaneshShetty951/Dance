# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_upcomingevents_eventorganiser'),
    ]

    operations = [
        migrations.AddField(
            model_name='upcomingevents',
            name='EventName',
            field=models.CharField(max_length=100, default='ABC'),
        ),
    ]
