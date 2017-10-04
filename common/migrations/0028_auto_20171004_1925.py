# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0027_facilityorgunitmapping'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='FacilityOrgUnitMapping',
            new_name='OrgUnitMapping',
        ),
        migrations.AlterModelOptions(
            name='orgunitmapping',
            options={'ordering': ('-updated', '-created'), 'default_permissions': ('add', 'change', 'delete', 'view'), 'verbose_name_plural': 'org_unit_mappings'},
        ),
    ]
