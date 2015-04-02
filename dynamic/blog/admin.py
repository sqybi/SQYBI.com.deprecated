from django.contrib import admin

import blog.models
import website.models


# Register your models here.
admin.site.register(website.models.User)
admin.site.register(website.models.UserRecord)
admin.site.register(blog.models.Article)
admin.site.register(blog.models.Comment)
