import datetime

from django.shortcuts import render
from django.template import RequestContext
import django.http
import ipware.ip

from user.models import User, UserRecord
import helper.constants
import helper.security


def login(request):
    if request.method == "POST":
        # make sure user name and password exist
        if "username" not in request.POST or "password" not in request.POST:
            return django.http.HttpResponseBadRequest()

        # validate username and password formats
        formatted_user_name = request.POST["username"].lower()
        if not helper.constants.user_name_pattern.match(formatted_user_name):
            return django.http.HttpResponseBadRequest()
        encrypted_password = helper.security.encrypt_password(request.POST["password"])

        # try to get user
        user = User.objects.filter(user_name=formatted_user_name, password=encrypted_password).first()
        if user is None:
            return django.http.HttpResponseBadRequest()

        # get user record
        user_record = UserRecord.objects.filter(user=user).first()
        if user_record is None:
            user_record = UserRecord(user=user, create_time=datetime.datetime.utcnow())

        user_record.last_login_ip = ipware.ip.get_real_ip(request)
        user_record.last_login_time = datetime.datetime.utcnow()
        user_record.cookie_token = helper.security.generate_cookie_token(user.user_name)

        # set session info
        request.session["user_name"] = formatted_user_name
        request.session["token"] = user_record.cookie_token

        # save models
        user_record.save()

        context = {
            "redirect_url": request.GET["return_url"] if "return_url" in request.GET else "/",
        }

        response = render(request, "auth/login.html", context)
        response.set_cookie("user_name", formatted_user_name, max_age=helper.constants.cookie_max_age_in_seconds,
                            httponly=True)
        response.set_cookie("token", user_record.cookie_token, max_age=helper.constants.cookie_max_age_in_seconds,
                            httponly=True)

        return response
    else:
        raise django.http.Http404


def logout(request):
    # all kinds of request methods are acceptable

    context = {
        "redirect_url": request.GET["return_url"] if "return_url" in request.GET else "/",
    }

    response = render(request, "auth/logout.html", context)
    response.delete_cookie("user_name")
    response.delete_cookie("token")
    del request.session["user_name"]
    del request.session["token"]
