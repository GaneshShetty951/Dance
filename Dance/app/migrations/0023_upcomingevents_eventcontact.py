# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0022_auto_20160708_2022'),
    ]

    operations = [
        migrations.AddField(
            model_name='upcomingevents',
            name='EventContact',
            field=models.CharField(blank=True, validators=[django.core.validators.RegexValidator(regex='^\\+?1?\\d{10}$', message="Phone number must be entered in the format: '1234567890'. Up to 10 digits allowed.")], max_length=10),
        ),
    ]
