# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_auto_20160522_1418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upcomingevents',
            name='EventImage',
            field=models.ImageField(blank=True, upload_to='.', null=True),
        ),
    ]
