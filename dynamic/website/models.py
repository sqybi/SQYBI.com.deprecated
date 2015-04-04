"""
Models for the whole website.
"""

from django.db import models
import user.models


# Base model for all items
class BaseItem(models.Model):
    create_time = models.DateTimeField()
    modify_time = models.DateTimeField()
    author = models.ForeignKey(user.models.User, null=True, on_delete=models.SET_NULL, related_name="items")

    class Meta():
        abstract = True