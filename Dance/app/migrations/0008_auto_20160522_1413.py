# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20160522_1409'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upcomingevents',
            name='EventPoster',
            field=models.ImageField(default='pic_folder/None/no-photo.jpg', upload_to='pic_folder/'),
        ),
    ]
