# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_upcomingevents_eventname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upcomingevents',
            name='EventImage',
            field=models.ImageField(default='/static/images/GSV.jpg', blank=True, null=True, upload_to='.'),
        ),
    ]
