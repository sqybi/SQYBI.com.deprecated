"""
Models for the whole website.
"""

from django.db import models


# Base model for all items
class BaseItem(models.Model):
    create_time = models.DateTimeField()
    modify_time = models.DateTimeField()
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    class Meta():
        abstract = True