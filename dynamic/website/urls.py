from django.conf.urls import patterns, include, url
from django.contrib import admin
import website.views
import auth.views
import user.views

admin.autodiscover()

urlpatterns = patterns(
    "",
    url(r"^$", website.views.home, name="home"),
    url(r"^admin/", include(admin.site.urls), name="admin"),
    url(r"^blog/", include("blog.urls", namespace="blog")),
    url(r"^login/", auth.views.login, name="login"),
    url(r"^logout/", auth.views.logout, name="logout"),
    url(r"^user/(?P<user_name>.+)$", user.views.user, name="user"),
)
