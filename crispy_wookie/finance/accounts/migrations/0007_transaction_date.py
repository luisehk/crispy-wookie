# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_transaction'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
