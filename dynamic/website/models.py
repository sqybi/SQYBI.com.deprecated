# This file contains models for the whole website

from django.db import models
import helper.password


# User information
class User(models.Model):
    user_name = models.CharField(max_length=50, unique=True, db_index=True)
    password = models.CharField(max_length=helper.password.encrypted_password_length, blank=False)
    is_admin = models.BooleanField(default=False)
    email = models.EmailField(max_length=100, blank=True)
    website = models.URLField(blank=True)
    description = models.CharField(max_length=100, blank=True)

    def __unicode__(self):
        return '%s:%s' % (self.id, self.user_name)


# Backend records for users
class UserRecord(models.Model):
    user = models.OneToOneField(User)
    last_login_ip = models.GenericIPAddressField(protocol='both', unpack_ipv4=True)
    last_login_time = models.DateTimeField()

    def __unicode__(self):
        return "%s:%s:%s" % (self.user, self.last_login_ip, self.last_login_time)


# Base model for all items
class BaseItem(models.Model):
    create_time = models.DateTimeField()
    modify_time = models.DateTimeField()
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    class Meta():
        abstract = True