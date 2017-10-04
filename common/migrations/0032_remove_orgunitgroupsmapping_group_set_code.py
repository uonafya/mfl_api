# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0031_auto_20171004_2016'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orgunitgroupsmapping',
            name='group_set_code',
        ),
    ]
