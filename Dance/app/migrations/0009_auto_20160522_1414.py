# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20160522_1413'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upcomingevents',
            name='EventPoster',
            field=models.ImageField(null=True, upload_to='pic_folder/', default='pic_folder/None/no-photo.jpg'),
        ),
    ]
