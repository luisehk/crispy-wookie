from django.db import models


class Category(models.Model):
    name = models.CharField(
        max_length=128,
        blank=False)

    def __unicode__(self):
        return self.name
