"""
Helper methods related to Authorization
"""

from user.models import User, UserRecord
import helper.constants
import helper.security


def get_current_user(request):
    user = None

    # try get user from session
    if "user_name" in request.session and "token" in request.session:
        user_name = request.session["user_name"]
        token = request.session["token"]
        user = get_user(user_name, token)[0]

    if user is not None:
        return user

    # try get user from cookie
    user_name = request.COOKIES.get("user_name")
    token = request.COOKIES.get("token")
    if user_name is not None and token is not None:
        result = get_user(user_name, token)
        user = result[0]
        user_record = result[1]
        if user is not None:
            # not exist in session, but exist in cookie: get new token and update
            user_record.cookie_token = helper.security.generate_cookie_token(user.user_name)
            user_record.save()
            request.COOKIES["token"] = user_record.cookie_token
            request.session["token"] = user_record.cookie_token

    if user is not None:
        user.user_path = user_name.replace('_', '-')

    return user


def get_user(user_name, token):
    user = None
    user_record = None

    if helper.constants.user_name_pattern.match(user_name):
        user = User.objects.filter(user_name=user_name).first()
        user_record = UserRecord.objects.filter(user=user).first()
        if user_record is None or user_record.cookie_token != token:
            user = None

    return user, user_record