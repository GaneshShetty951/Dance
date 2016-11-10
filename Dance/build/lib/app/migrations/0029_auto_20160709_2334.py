# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0028_upcomingevents_eventlink'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upcomingevents',
            name='EventLink',
            field=models.URLField(default='#'),
        ),
    ]
