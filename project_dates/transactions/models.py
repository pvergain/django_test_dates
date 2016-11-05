#!/usr/bin/python
# -*- coding: utf8 -*-
"""


"""
import uuid

# https://docs.djangoproject.com/en/dev/ref/models/
from django.db import models

class Transaction(models.Model):

    # https://docs.djangoproject.com/en/dev/ref/models/options
    class Meta:
        verbose_name = 'Transaction'
        verbose_name_plural = 'Transactions'
        # https://docs.djangoproject.com/en/dev/ref/models/options/#managed
        managed = True

    id = models.AutoField(
        # https://docs.djangoproject.com/en/dev/ref/models/fields/#primary-key
        primary_key=True,
    )

    # https://docs.djangoproject.com/en/dev/ref/models/fields/#uuidfield
    uid = models.UUIDField(
        unique=True,
        editable=False,
        default=uuid.uuid4,
        verbose_name='Public identifier',
    )

    # https://docs.djangoproject.com/en/dev/ref/models/fields/#charfield
    sender = models.CharField(
        max_length=200,
        verbose_name="The sender identifier"
    )
    # https://docs.djangoproject.com/en/dev/ref/models/fields/#DateTimeField
    created = models.DateTimeField(
        blank=True,
        verbose_name="The transaction creation date",
    )

    def __str__(self):
        return self.name


    def get_absolute_url(self):
        """
        https://docs.djangoproject.com/en/dev/ref/class-based-views/generic-editing/
        """
        return reverse('transactions:detail',
                       kwargs={'pk': self.pk})


