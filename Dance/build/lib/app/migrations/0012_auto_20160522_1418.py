# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20160522_1416'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upcomingevents',
            name='EventImage',
            field=models.ImageField(upload_to='/pic_folder/', default='/pic_folder/None/no-photo.jpg'),
        ),
    ]
