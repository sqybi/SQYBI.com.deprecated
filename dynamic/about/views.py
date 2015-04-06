from django.shortcuts import render
import django.http

import helper.auth
import helper.general


def index(request):
    if request.method == "GET":
        user = helper.auth.get_current_user(request)

        context = {
            "title": "About | SQYBI.com",
            "app": "about",
            "user": user,
            "request": request,
            "alert_level": helper.general.get_alert_level(request),
            "alert_message": helper.general.get_alert_message(request),
        }

        return render(request, "about/index.html", context)
    else:
        raise django.http.Http404