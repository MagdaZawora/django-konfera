# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-17 14:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('konfera', '0033_auto_20170215_1932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receipt',
            name='taxid',
            field=models.CharField(blank=True, max_length=32, verbose_name='TAX ID'),
        ),
    ]
