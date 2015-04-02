# This is for encrypting the password with hash algorithms and salt

import hashlib


encrypted_password_length = hashlib.sha1().digest_size * 2


def encrypt(raw_password, salt="", encrypt_round=1):
    result = raw_password
    for i in range(encrypt_round):
        result = encrypt_once(result, salt)
    return result


def encrypt_once(raw_password, salt=""):
    hash_algorithm = hashlib.sha1()
    hash_algorithm.update(salt)
    hash_algorithm.update(raw_password)
    return hash_algorithm.hexdigest()
