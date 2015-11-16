# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20151115_2040'),
    ]

    operations = [
        migrations.CreateModel(
            name='CreditAccount',
            fields=[
                ('account_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='accounts.Account')),
                ('limit', models.DecimalField(default=0.0, max_digits=18, decimal_places=2)),
                ('annual_percentage_rate', models.DecimalField(default=0.0, max_digits=3, decimal_places=2)),
                ('due_date', models.DateField()),
            ],
            options={
                'ordering': ['name', 'balance'],
            },
            bases=('accounts.account',),
        ),
        migrations.CreateModel(
            name='DebitCard',
            fields=[
                ('account_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='accounts.Account')),
            ],
            bases=('accounts.account',),
        ),
        migrations.CreateModel(
            name='CreditCard',
            fields=[
                ('creditaccount_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='accounts.CreditAccount')),
                ('statement_balance', models.DecimalField(default=0.0, max_digits=18, decimal_places=2)),
                ('minimum_payment', models.DecimalField(default=0.0, max_digits=18, decimal_places=2)),
                ('closing_date', models.DateField()),
            ],
            bases=('accounts.creditaccount',),
        ),
    ]
