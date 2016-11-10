# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_auto_20160616_1124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upcomingevents',
            name='EventImage',
            field=models.ImageField(blank=True, null=True, upload_to='.'),
        ),
    ]
