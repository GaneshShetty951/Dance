# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0021_auto_20160701_1256'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='upcomingevents',
            name='EventType',
        ),
        migrations.AlterField(
            model_name='upcomingevents',
            name='ShowCategory',
            field=models.CharField(choices=[('Free', 'Free'), ('Passes', 'Passes'), ('Private', 'Private')], max_length=1),
        ),
    ]
