# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('id_generate', '0040_auto_20160303_1318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jaxiddetail',
            name='entered_into_lims',
            field=models.BooleanField(default=False, help_text='Entered into LIMS', verbose_name='Entered into LIMS'),
        ),
        migrations.AlterField(
            model_name='jaxiddetail',
            name='external_data',
            field=models.BooleanField(default=False, help_text='External data (not sequenced here.)', verbose_name='External data (not sequenced here.)'),
        ),
    ]