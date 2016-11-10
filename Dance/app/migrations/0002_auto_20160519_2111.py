# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('Artist_name', models.CharField(null=True, max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='upcomingevents',
            name='id',
        ),
        migrations.AddField(
            model_name='upcomingevents',
            name='EventPoster',
            field=models.ImageField(default=None, upload_to=''),
        ),
        migrations.AlterField(
            model_name='upcomingevents',
            name='EventDate',
            field=models.DateTimeField(primary_key=True, default=datetime.datetime(2016, 5, 19, 15, 41, 6, 882386, tzinfo=utc), serialize=False),
        ),
        migrations.AlterField(
            model_name='upcomingevents',
            name='EventVenue',
            field=models.CharField(default='Bangalore', max_length=100),
        ),
        migrations.AddField(
            model_name='artist',
            name='EventDate',
            field=models.ForeignKey(to='app.UpComingEvents'),
        ),
    ]
