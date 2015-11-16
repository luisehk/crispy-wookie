from django.test import TestCase
from .models import Category


class CategoryTest(TestCase):
    def create_category(self, name):
        return Category.objects.create(name=name)

    def test_category_creation(self):
        name = 'My new category'

        a = self.create_category(name=name)

        self.assertTrue(isinstance(a, Category))
        self.assertEqual(a.__unicode__(), a.name)
