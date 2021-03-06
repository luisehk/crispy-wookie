from django.contrib.auth.models import User
from ..budget.models import Category
from django.utils import timezone
from django.db import models


def money_field():
    return models.DecimalField(
        max_digits=18,
        decimal_places=2,
        default=0.00)


class Account(models.Model):
    user = models.ForeignKey(
        User,
        null=True)
    name = models.CharField(
        max_length=128,
        blank=False)
    balance = money_field()

    class Meta:
        ordering = ['name', '-balance']

    def __unicode__(self):
        return self.name


class DebitCard(Account):
    pass


class CreditAccount(Account):
    limit = money_field()
    annual_percentage_rate = models.DecimalField(
        max_digits=3,
        decimal_places=2,
        default=0.00)
    due_date = models.DateField()

    class Meta:
        ordering = ['name', 'balance']


class CreditCard(CreditAccount):
    statement_balance = money_field()
    minimum_payment = money_field()
    closing_date = models.DateField()


class Transaction(models.Model):
    origin = models.ForeignKey(
        Account,
        related_name='origin',
        null=True)
    destination = models.ForeignKey(
        Account,
        related_name='destination',
        null=True)
    description = models.CharField(
        max_length=128,
        blank=True)
    category = models.ForeignKey(
        Category,
        null=True)
    amount = money_field()
    date = models.DateField(
        default=timezone.now)
