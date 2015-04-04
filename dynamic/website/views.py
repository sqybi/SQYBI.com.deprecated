from django.shortcuts import render
import random

import helper.constants


def home(request):
    context = {
        "title": "Home | SQYBI.com",
        "app": "Home",
        "alert_level": helper.constants.alert_level,
        "alert_message": helper.constants.alert_message,
        "daily_quote": random.choice(helper.constants.daily_quotes)
    }

    return render(request, "website/index.html", context)