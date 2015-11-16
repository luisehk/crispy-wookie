# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0001_initial'),
        ('accounts', '0005_auto_20151116_0348'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=128, blank=True)),
                ('amount', models.DecimalField(default=0.0, max_digits=18, decimal_places=2)),
                ('category', models.ForeignKey(to='budget.Category', null=True)),
                ('destination', models.ForeignKey(related_name='destination', to='accounts.Account', null=True)),
                ('origin', models.ForeignKey(related_name='origin', to='accounts.Account', null=True)),
            ],
        ),
    ]
