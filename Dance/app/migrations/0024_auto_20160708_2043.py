# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0023_upcomingevents_eventcontact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upcomingevents',
            name='ShowCategory',
            field=models.CharField(max_length=1, default='Free', choices=[('Free', 'Free'), ('Passes', 'Passes'), ('Private', 'Private')]),
        ),
    ]
