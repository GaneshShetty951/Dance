# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0025_auto_20160708_2051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upcomingevents',
            name='EventContact',
            field=models.CharField(blank=True, max_length=10, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '1234567890'. Up to 10 digits allowed.", regex='^\\?\\d{10}$')]),
        ),
    ]
