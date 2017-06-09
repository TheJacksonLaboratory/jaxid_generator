# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-09 18:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('id_generate', '0063_auto_20170503_1349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jaxiddetail',
            name='parent_jaxid',
            field=models.CharField(default='', help_text="Parent ID string of source JAXid; or use 'received' for newly received samples,'pool' for pools of libraries.", max_length=9, verbose_name='Parent JAXid'),
        ),
    ]