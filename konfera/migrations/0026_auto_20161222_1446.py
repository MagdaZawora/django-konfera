# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-22 14:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('konfera', '0025_organizer_other'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sponsor',
            name='type',
            field=models.IntegerField(choices=[(1, 'Platinum'), (2, 'Gold'), (3, 'Silver'), (4, 'Bronze'), (7, 'Media'), (5, 'Other'), (6, 'Django girls')]),
        ),
    ]
