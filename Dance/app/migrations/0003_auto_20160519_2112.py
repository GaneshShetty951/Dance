# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20160519_2111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upcomingevents',
            name='EventDate',
            field=models.DateTimeField(serialize=False, primary_key=True),
        ),
    ]
