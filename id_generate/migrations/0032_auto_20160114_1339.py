# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('id_generate', '0031_auto_20160114_1338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jaxidmasterlist',
            name='jaxid',
            field=models.ForeignKey(to='id_generate.JAXIdDetail', to_field='jaxid', on_delete=django.db.models.deletion.PROTECT),
        ),
    ]