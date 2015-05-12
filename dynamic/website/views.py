from django.shortcuts import render
import django.http
import random

import helper.constants
import helper.security
import helper.auth
import helper.general


def home(request):
    if request.method == "GET":
        random_quote = random.choice(helper.constants.daily_quotes)

        user, new_token = helper.auth.get_current_user(request)

        context = {
            "title": "Home | SQYBI.com",
            "app": "home",
            "user": user,
            "request": request,
            "alert_level": helper.general.get_alert_level(request),
            "alert_message": helper.general.get_alert_message(request),
            "daily_quote": random_quote[0],
            "daily_quote_author": random_quote[1],
        }

        response = render(request, "website/index.html", context)
        if new_token is not None:
            response.set_cookie("token", new_token, max_age=helper.constants.cookie_max_age_in_seconds, httponly=True)
        return response
    else:
        return django.http.HTTP404
