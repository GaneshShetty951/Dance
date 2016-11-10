# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0024_auto_20160708_2043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upcomingevents',
            name='EventContact',
            field=models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(regex='^\\?1?\\d{10}$', message="Phone number must be entered in the format: '1234567890'. Up to 10 digits allowed.")], blank=True),
        ),
        migrations.AlterField(
            model_name='upcomingevents',
            name='ShowCategory',
            field=models.CharField(max_length=7, choices=[('Free', 'Free'), ('Passes', 'Passes'), ('Private', 'Private')], default='Free'),
        ),
    ]
