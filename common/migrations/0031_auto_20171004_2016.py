# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0030_auto_20171004_1946'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orgunitgroupsmapping',
            old_name='group_set_id',
            new_name='group_set_ids',
        ),
        migrations.RemoveField(
            model_name='orgunitgroupsmapping',
            name='group_set_name',
        ),
    ]
