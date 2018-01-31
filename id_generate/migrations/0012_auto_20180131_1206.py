# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-31 12:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('id_generate', '0011_auto_20180131_1127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boxid',
            name='nucleic_acid_type',
            field=models.ForeignKey(default='Z', on_delete=django.db.models.deletion.CASCADE, to='id_generate.NucleicAcidType', to_field='code', verbose_name='Nucleic Acid'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='boxid',
            name='sequencing_type',
            field=models.ForeignKey(default='Z', on_delete=django.db.models.deletion.CASCADE, to='id_generate.SequencingType', to_field='code'),
            preserve_default=False,
        ),
    ]