from django.db import models


class Account(models.Model):
    name = models.CharField(
        max_length=128,
        blank=False)
    balance = models.DecimalField(
        max_digits=18,
        decimal_places=2,
        default=0.00)

    class Meta:
        abstract = False
        ordering = ['name', '-balance']

    def __unicode__(self):
        return self.name
