from django.conf.urls import patterns, include, url
from django.contrib import admin
import website.views
import siteauth.views
import user.views
import about.views

admin.autodiscover()

urlpatterns = patterns(
    "",
    url(r"^$", website.views.home, name="home"),
    url(r"^admin/", include(admin.site.urls), name="admin"),
    url(r"^blog/", include("blog.urls", namespace="blog")),
    url(r"^login/", siteauth.views.login, name="login"),
    url(r"^logout/", siteauth.views.logout, name="logout"),
    url(r"^register/", siteauth.views.register, name="register"),
    url(r"^about/", about.views.index, name="about"),
    url(r"^user/(?P<user_path>[a-zA-Z0-9\-]+)$", user.views.user, name="user"),
)
