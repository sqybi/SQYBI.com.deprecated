from django.db import models
import helper.security


# User information (Information which is provided by user)
class User(models.Model):
    user_name = models.CharField(max_length=20, unique=True, db_index=True)
    password = models.CharField(max_length=helper.security.encrypted_password_length, blank=False)
    is_admin = models.BooleanField(default=False)
    display_name = models.CharField(max_length=50, unique=True, db_index=True)
    email = models.EmailField(max_length=100, blank=True)
    website = models.URLField(blank=True)
    description = models.CharField(max_length=100, blank=True)

    def __unicode__(self):
        return "%s:%s" % (self.id, self.user_name)


# Backend records for users (Information which is generated automatically)
class UserRecord(models.Model):
    user = models.OneToOneField(User)
    create_time = models.DateTimeField()
    last_login_ip = models.GenericIPAddressField(protocol="both", unpack_ipv4=True)
    last_login_time = models.DateTimeField()
    cookie_token = models.CharField(max_length=helper.security.token_length, blank=True)

    def __unicode__(self):
        return "%s:%s:%s" % (self.user, self.last_login_ip, self.last_login_time)
