# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-19 00:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0007_remove_trip_destination'),
    ]

    operations = [
        migrations.AddField(
            model_name='tripmember',
            name='email',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
