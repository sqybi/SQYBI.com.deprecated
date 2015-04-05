from django.shortcuts import render
import django.http
import random

import helper.constants
import helper.security
import helper.auth


def home(request):
    if request.method == "GET":
        random_quote = random.choice(helper.constants.daily_quotes)

        user = helper.auth.get_current_user(request)

        context = {
            "title": "Home | SQYBI.com",
            "app": "Home",
            "user": user,
            "request": request,
            "alert_level": helper.constants.alert_level,
            "alert_message": helper.constants.alert_message,
            "daily_quote": random_quote[0],
            "daily_quote_author": random_quote[1],
        }

        return render(request, "website/index.html", context)
    else:
        return django.http.HTTP404
