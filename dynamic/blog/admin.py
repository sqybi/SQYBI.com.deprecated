from django.contrib import admin

import blog.models
import website.models
import user.models


# Register your models here.
admin.site.register(user.models.User)
admin.site.register(user.models.UserRecord)
admin.site.register(website.models.BaseItem)
admin.site.register(blog.models.BlogArticleItem)
admin.site.register(blog.models.BlogCommentItem)
