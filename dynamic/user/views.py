from django.shortcuts import render, redirect, get_object_or_404
import django.http

from user.models import User
import helper.constants
import helper.auth
import helper.general


def user(request, user_path=None):
    if request.method == "GET":
        user_name = user_path.replace('-', '_')
        if not helper.constants.user_name_pattern.match(user_name):
            raise django.http.Http404
        display_user = get_object_or_404(User, user_name=user_name)

        recent_blog_articles = display_user.blogarticleitems.filter(is_shown=True).order_by("id").reverse()[:helper.constants.user_recent_blog_article_count]
        recent_blog_comments = display_user.blogcommentitems.filter(article__is_shown=True).order_by("id").reverse()[:helper.constants.user_recent_blog_comment_count]

        user, new_token = helper.auth.get_current_user(request)

        context = {
            "title": display_user.display_name + " | User Page | SQYBI.com",
            "app": "user",
            "user": user,
            "request": request,
            "alert_level": helper.general.get_alert_level(request),
            "alert_message": helper.general.get_alert_message(request),
            "display_user": display_user,
            "recent_blog_articles": recent_blog_articles,
            "recent_blog_comments": recent_blog_comments,
        }

        response = render(request, "user/userpage.html", context)
        if new_token is not None:
            response.set_cookie("token", new_token, max_age=helper.constants.cookie_max_age_in_seconds, httponly=True)
        return response
    else:
        return django.http.Http404