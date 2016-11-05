#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""Transaction Administration.

"""

from django.contrib import admin

from .models import Transaction

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    """Transaction administration

    Documentation
    =============

    - https://docs.djangoproject.com/en/dev/ref/contrib/admin/#modeladmin-objects

    """
    date_hierarchy = 'created'
    list_display = ('uid', 'sender', 'created')
    search_fields = ('uid', 'sender', 'created')
    list_filter = ('uid', 'sender', 'created')
