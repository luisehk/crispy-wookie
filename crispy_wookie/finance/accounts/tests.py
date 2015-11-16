from django.test import TestCase
from .models import Account


class AccountTest(TestCase):
    def create_account(self, name, balance):
        return Account.objects.create(
            name=name,
            balance=balance)

    def test_account_creation(self):
        name = 'My checking account'
        balance = 1025.05

        a = self.create_account(
            name=name,
            balance=balance)

        self.assertTrue(isinstance(a, Account))
        self.assertEqual(a.__unicode__(), a.name)
        self.assertEqual(balance, a.balance)
