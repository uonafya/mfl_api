# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0032_remove_orgunitgroupsmapping_group_set_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orgunitgroupsmapping',
            name='group_set_ids',
            field=models.TextField(null=True, blank=True),
        ),
    ]
