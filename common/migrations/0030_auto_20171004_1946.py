# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0029_auto_20171004_1927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='constituencymapping',
            name='mfl_code',
            field=models.IntegerField(default=0, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='constituencymapping',
            name='mfl_name',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='countymapping',
            name='mfl_code',
            field=models.IntegerField(default=0, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='countymapping',
            name='mfl_name',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='orgunitgroupsmapping',
            name='mfl_code',
            field=models.IntegerField(default=0, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='orgunitgroupsmapping',
            name='mfl_name',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='subcountymapping',
            name='mfl_code',
            field=models.IntegerField(default=0, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='subcountymapping',
            name='mfl_name',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='wardmapping',
            name='mfl_code',
            field=models.IntegerField(default=0, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='wardmapping',
            name='mfl_name',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
    ]
