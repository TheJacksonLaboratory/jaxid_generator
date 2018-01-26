# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-26 09:14
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('id_generate', '0005_auto_20180126_0912'),
    ]

    operations = [
        migrations.CreateModel(
            name='BoxId',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parent_id', models.CharField(blank=True, default='', max_length=6, null=True, verbose_name='Parent id')),
                ('name', models.TextField(verbose_name='Name')),
                ('external_data', models.NullBooleanField(default=False, help_text='(not sequenced here.)', verbose_name='External data')),
                ('notes', models.TextField(blank=True, null=True, verbose_name='Notes')),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('boxid', models.CharField(max_length=6, unique=True, validators=[django.core.validators.MinLengthValidator(6)], verbose_name='BoxID')),
                ('nucleic_acid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='id_generate.NucleicAcidType', to_field='code', verbose_name='Nucleic Acid Type')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='id_generate.ProjectCode', to_field='code', verbose_name='Project')),
                ('sample', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='id_generate.SampleType', to_field='code', verbose_name='Sample Type')),
                ('seq_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='id_generate.SequencingType', to_field='code', verbose_name='Sequencing Type')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
