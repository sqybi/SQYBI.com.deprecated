from django.db import models

# Create your models here.

# User information
class User(models.Model):
    user_name = models.CharField(max_length = 50, unique = True, db_index = True)
    is_admin = models.BooleanField()
    email = models.EmailField(max_length = 100)
    website = models.URLField(blank = True)
    description = models.CharField(max_length = 1000, blank = True)

    def __unicode__(self):
        return '%s:%s' % (self.id, self.user_name)

# Backend records for users
class UserRecord(models.Model):
    user = models.OneToOneField('User')
    last_login_ip = models.GenericIPAddressField(protocol = 'both', unpack_ipv4 = True)
    last_login_time = models.DateTimeField()

    def __unicode__(self):
        return "%s:%s:%s" % (self.user, self.last_login_ip, self.last_login_time)

# Blog articles
class Article(models.Model):
    slug = models.SlugField(max_length = 100, unique = True, db_index = True)
    title = models.CharField(max_length = 100)
    markdown_content = models.TextField(blank = True)
    html_content = models.TextField(blank = True)
    published_time = models.DateTimeField()
    last_modified_time = models.DateTimeField()
    is_shown = models.BooleanField()

    def __unicode__(self):
        return "%s:%s" % (self.id, self.title)

# Comments
class Comment(models.Model):
    related_article = models.ForeignKey('Article')
    is_registered_user = models.BooleanField()
    user_id = models.ForeignKey('User', null = True)
    name = models.CharField(max_length = 50, null = True)
    email = models.EmailField(max_length = 100, null = True, blank = True)
    website = models.URLField(null = True, blank = True)
    content = models.TextField()

    def __unicode__(self):
        return "%s:%s" % (self.id, self.related_article_id)

