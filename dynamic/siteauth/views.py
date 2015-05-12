import datetime
import urllib

from django.shortcuts import render, redirect
import django.http
import ipware.ip

from user.models import User, UserRecord
import helper.constants
import helper.security
import helper.auth
import helper.general


def login(request):
    if request.method == "GET":
        return_url = request.GET["return_url"] if "return_url" in request.GET else "/"

        user, new_token = helper.auth.get_current_user(request)

        if user is not None:
            response = redirect(helper.general.get_redirect_url(return_url, (
                { "key": "alertlevel", "value": "warning" },
                { "key": "alertmsg", "value": "Already signed in" })))
            if new_token is not None:
                response.set_cookie("token", new_token, max_age=helper.constants.cookie_max_age_in_seconds, httponly=True)
            return response

        context = {
            "title": "Login | SQYBI.com",
            "app": "auth",
            "user": user,
            "request": request,
            "alert_level": helper.general.get_alert_level(request),
            "alert_message": helper.general.get_alert_message(request),
            "return_url": return_url,
        }

        return render(request, "auth/login.html", context)

    elif request.method == "POST":
        return_url_success = request.GET["return_url"] if "return_url" in request.GET else "/"
        return_url_failed = request.META["HTTP_REFERER"] if "HTTP_REFERER" in request.META else "/"

        user, new_token = helper.auth.get_current_user(request)

        if user is not None:
            response = redirect(helper.general.get_redirect_url(return_url_failed, (
                { "key": "alertlevel", "value": "warning" },
                { "key": "alertmsg", "value": "Already signed in" })))
            if new_token is not None:
                response.set_cookie("token", new_token, max_age=helper.constants.cookie_max_age_in_seconds, httponly=True)
            return response

        # make sure user name and password exist
        if "username" not in request.POST or "password" not in request.POST:
            return redirect(helper.general.get_redirect_url(return_url_failed, (
                { "key": "alertlevel", "value": "error" },
                { "key": "alertmsg", "value": "Empty username or password is not allowed" })))

        # validate username and password formats
        formatted_user_name = request.POST["username"].lower()
        if not helper.constants.user_name_pattern.match(formatted_user_name):
            return redirect(helper.general.get_redirect_url(return_url_failed, (
                { "key": "alertlevel", "value": "error" },
                { "key": "alertmsg", "value": "Wrong username or password" })))
        encrypted_password = helper.security.encrypt_password(request.POST["password"])

        # try to get user
        user = User.objects.filter(user_name=formatted_user_name, password=encrypted_password).first()
        if user is None:
            return redirect(helper.general.get_redirect_url(return_url_failed, (
                { "key": "alertlevel", "value": "error" },
                { "key": "alertmsg", "value": "Wrong username or password" })))

        # get user record
        user_record = UserRecord.objects.filter(user=user).first()
        if user_record is None:
            user_record = UserRecord(user=user, create_time=datetime.datetime.utcnow())

        user_record.last_login_ip = ipware.ip.get_real_ip(request)
        user_record.last_login_time = datetime.datetime.utcnow()
        user_record.cookie_token = helper.security.generate_cookie_token(user.user_name)

        # save models
        user_record.save()

        # set session info
        request.session["user_name"] = formatted_user_name
        request.session["token"] = user_record.cookie_token

        response = redirect(return_url_success)

        if "remember" in request.POST:
            response.set_cookie("user_name", formatted_user_name, max_age=helper.constants.cookie_max_age_in_seconds,
                                httponly=True)
            response.set_cookie("token", user_record.cookie_token, max_age=helper.constants.cookie_max_age_in_seconds,
                                httponly=True)

        return response

    else:
        return django.http.HttpResponseBadRequest()


def logout(request):
    # all kinds of request methods are acceptable

    return_url = request.GET["return_url"] if "return_url" in request.GET else "/"

    response = redirect(return_url)
    response.delete_cookie("user_name")
    response.delete_cookie("token")
    try:
        del request.session["user_name"]
        del request.session["token"]
    except KeyError:
        pass

    return response


def register(request):
    if request.method == "GET":
        return_url = request.GET["return_url"] if "return_url" in request.GET else "/"

        user, new_token = helper.auth.get_current_user(request)

        if user is not None:
            response = redirect(helper.general.get_redirect_url(return_url, (
                { "key": "alertlevel", "value": "warning" },
                { "key": "alertmsg", "value": "Already signed in" })))
            if new_token is not None:
                response.set_cookie("token", new_token, max_age=helper.constants.cookie_max_age_in_seconds, httponly=True)
            return response

        context = {
            "title": "Register | SQYBI.com",
            "app": "auth",
            "user": user,
            "request": request,
            "alert_level": helper.general.get_alert_level(request),
            "alert_message": helper.general.get_alert_message(request),
            "return_url": return_url,
        }

        return render(request, "auth/register.html", context)

    elif request.method == "POST":
        return_url_success = request.GET["return_url"] if "return_url" in request.GET else "/"
        return_url_failed = request.META["HTTP_REFERER"] if "HTTP_REFERER" in request.META else "/"

        user, new_token = helper.auth.get_current_user(request)

        if user is not None:
            response = redirect(helper.general.get_redirect_url(return_url_failed, (
                { "key": "alertlevel", "value": "warning" },
                { "key": "alertmsg", "value": "Already signed in" })))
            if new_token is not None:
                response.set_cookie("token", new_token, max_age=helper.constants.cookie_max_age_in_seconds, httponly=True)
            return response

        # make sure required fields exist
        if "username" not in request.POST or "password" not in request.POST or "displayname" not in request.POST:
            return redirect(helper.general.get_redirect_url(return_url_failed, (
                { "key": "alertlevel", "value": "error" },
                { "key": "alertmsg", "value": "Required fields must not be empty" })))

        # validate username and password formats
        formatted_user_name = request.POST["username"].lower()
        if not helper.constants.user_name_pattern.match(formatted_user_name):
            return redirect(helper.general.get_redirect_url(return_url_failed, (
                { "key": "alertlevel", "value": "error" },
                { "key": "alertmsg", "value": "User name in wrong format" })))

        if len(request.POST["password"]) < helper.constants.password_min_length:
            return redirect(helper.general.get_redirect_url(return_url_failed, (
                { "key": "alertlevel", "value": "error" },
                { "key": "alertmsg", "value": "Password is too short, must contain at least " + str(helper.constants.password_min_length) + " characters" })))
        encrypted_password = helper.security.encrypt_password(request.POST["password"])

        # try to get user
        if User.objects.filter(user_name=formatted_user_name).count() > 0:
            return redirect(helper.general.get_redirect_url(return_url_failed, (
                { "key": "alertlevel", "value": "error" },
                { "key": "alertmsg", "value": "User already exists" })))

        # create user
        user = User(user_name=formatted_user_name, password=encrypted_password,
                    display_name=request.POST["displayname"])
        user.user_path = helper.general.get_user_path(formatted_user_name)
        user.is_admin = False
        user.email = request.POST["email"] if "email" in request.POST else ""
        user.website = request.POST["website"] if "website" in request.POST else ""
        user.description = request.POST["quote"] if "quote" in request.POST else ""
        user.save()

        # create user record
        user_record = UserRecord(user=user, create_time=datetime.datetime.utcnow())
        user_record.last_login_ip = ipware.ip.get_real_ip(request)
        user_record.last_login_time = datetime.datetime.utcnow()
        user_record.cookie_token = helper.security.generate_cookie_token(user.user_name)
        user_record.save()

        # set session info
        request.session["user_name"] = formatted_user_name
        request.session["token"] = user_record.cookie_token

        # do not set cookie for response
        response = redirect(return_url_success)
        return response

    else:
        return django.http.HttpResponseBadRequest()