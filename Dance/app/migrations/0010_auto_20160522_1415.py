# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20160522_1414'),
    ]

    operations = [
        migrations.RenameField(
            model_name='upcomingevents',
            old_name='EventPoster',
            new_name='EventImage',
        ),
    ]
