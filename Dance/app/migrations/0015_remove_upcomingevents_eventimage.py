# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_auto_20160522_1445'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='upcomingevents',
            name='EventImage',
        ),
    ]
