# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0026_auto_20171003_1201'),
    ]

    operations = [
        migrations.CreateModel(
            name='FacilityOrgUnitMapping',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('mfl_name', models.CharField(max_length=255)),
                ('mfl_code', models.IntegerField(default=0)),
                ('dhis_name', models.CharField(max_length=255, null=True, blank=True)),
                ('dhis_id', models.CharField(max_length=255, null=True, blank=True)),
                ('dhis_parent_id', models.CharField(max_length=255, null=True, blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('group_set_name', models.CharField(max_length=255, null=True, blank=True)),
                ('group_set_id', models.CharField(max_length=255, null=True, blank=True)),
                ('group_set_code', models.CharField(max_length=255, null=True, blank=True)),
                ('group_code', models.CharField(max_length=255, null=True, blank=True)),
            ],
            options={
                'ordering': ('-updated', '-created'),
                'default_permissions': ('add', 'change', 'delete', 'view'),
                'abstract': False,
                'verbose_name_plural': 'facility_org_unit_mappings',
            },
        ),
    ]
