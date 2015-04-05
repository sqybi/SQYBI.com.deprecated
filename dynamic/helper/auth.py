"""
Helper methods related to Authorization
"""

from user.models import User, UserRecord
import helper.constants


def get_current_user(request):
    user = None

    # try get user from session
    if "user_name" in request.session and "token" in request.session:
        user_name = request.session["user_name"]
        token = request.session["token"]
        user = get_user(user_name, token)

    if user is not None:
        return user

    # try get user from cookie
    user_name = request.COOKIES.get("user_name")
    token = request.COOKIES.get("token")
    if user_name is not None and token is not None:
        user = get_user(user_name, token)

    return user


def get_user(user_name, token):
    user = None

    if helper.constants.user_name_pattern.match(user_name):
        user = User.objects.filter(user_name=user_name).first()
        if UserRecord.objects.filter(user=user).first().cookie_token != token:
            user = None

    return user