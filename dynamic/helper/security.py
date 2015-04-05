"""
Helper methods related to security.

Encrypting the password, generating token for cookie, etc.
"""

import hashlib
import datetime

import helper.constants
from user.models import User, UserRecord


encrypted_password_length = hashlib.sha1().digest_size * 2

token_length = hashlib.sha1().digest_size * 2


def encrypt_password(raw_password, salt=helper.constants.salt_base, encrypt_round=helper.constants.password_encrypt_round):
    result = raw_password
    for i in range(encrypt_round):
        result = encrypt_password_once(result, salt)
    return result


def encrypt_password_once(raw_password, salt=helper.constants.salt_base):
    hash_algorithm = hashlib.sha1()
    hash_algorithm.update(salt)
    hash_algorithm.update(raw_password)
    return hash_algorithm.hexdigest()


def generate_salt():
    hash_algorithm = hashlib.sha1()
    hash_algorithm.update(helper.constants.salt_base)
    hash_algorithm.update(str(datetime.datetime.utcnow()))


def generate_cookie_token(user_name):
    hash_algorithm = hashlib.sha1()
    hash_algorithm.update(user_name)
    hash_algorithm.update(str(datetime.datetime.utcnow()))
    return hash_algorithm.hexdigest()


def get_current_user(request):
    user = None

    # try get user from session
    if "user_name" in request.session and "token" in request.session:
        user_name = request.session["user_name"]
        token = request.session["token"]
        user = get_user(user_name, token)

    if user is not None:
        return user;

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

    return user;