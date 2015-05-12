from django.shortcuts import render
import django.http

import helper.auth
import helper.general


def index(request):
    if request.method == "GET":
        user, new_token = helper.auth.get_current_user(request)

        context = {
            "title": "About | SQYBI.com",
            "app": "about",
            "user": user,
            "request": request,
            "alert_level": helper.general.get_alert_level(request),
            "alert_message": helper.general.get_alert_message(request),
        }

        response = render(request, "about/index.html", context)
        if new_token is not None:
            response.set_cookie("token", new_token, max_age=helper.constants.cookie_max_age_in_seconds, httponly=True)
        return response

    else:
        raise django.http.Http404