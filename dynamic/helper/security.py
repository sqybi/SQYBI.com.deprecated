"""
Helper methods related to security.

Encrypting the password, generating token for cookie, etc.
"""

import hashlib
import datetime

import helper.constants


encrypted_password_length = hashlib.sha1().digest_size * 2

token_length = hashlib.sha1().digest_size * 2


def encrypt_password(raw_password, salt="", encrypt_round=1):
    result = raw_password
    for i in range(encrypt_round):
        result = encrypt_password_once(result, salt)
    return result


def encrypt_password_once(raw_password, salt=""):
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