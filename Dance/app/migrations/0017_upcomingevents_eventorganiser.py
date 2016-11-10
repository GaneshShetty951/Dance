# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_upcomingevents_eventimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='upcomingevents',
            name='EventOrganiser',
            field=models.CharField(default='XYZ', max_length=100),
        ),
    ]
