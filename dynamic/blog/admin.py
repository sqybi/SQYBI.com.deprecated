from django.contrib import admin
import blog.models

# Register your models here.
admin.site.register(blog.models.User)
admin.site.register(blog.models.UserRecord)
admin.site.register(blog.models.Article)
admin.site.register(blog.models.Comment)
