# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20160522_1415'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upcomingevents',
            name='EventImage',
            field=models.ImageField(default='/pic_folder/None/no-photo.jpg', null=True, upload_to='/pic_folder/'),
        ),
    ]
