# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0028_auto_20171004_1925'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='OrgUnitMapping',
            new_name='OrgUnitGroupsMapping',
        ),
        migrations.AlterModelOptions(
            name='orgunitgroupsmapping',
            options={'ordering': ('-updated', '-created'), 'default_permissions': ('add', 'change', 'delete', 'view'), 'verbose_name_plural': 'org_unit_groups_mappings'},
        ),
    ]
