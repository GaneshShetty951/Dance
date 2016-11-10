# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_remove_upcomingevents_eventimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='upcomingevents',
            name='EventImage',
            field=models.ImageField(null=True, blank=True, upload_to='.'),
        ),
    ]
