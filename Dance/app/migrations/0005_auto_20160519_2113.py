# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20160519_2113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upcomingevents',
            name='EventPoster',
            field=models.ImageField(upload_to='', null=True),
        ),
    ]
