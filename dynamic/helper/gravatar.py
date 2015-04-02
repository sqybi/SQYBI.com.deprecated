"""
Helper methods related to Gravatar
"""

import hashlib


# public methods


def get_image_url(email_address, size=None):
    email_hash = __get_email_hash(email_address)
    url = "http://www.gravatar.com/avatar/" + email_hash
    if size is not None:
        url += "?s=" + size
    return url


def get_profile_url(email_address):
    email_hash = email_address
    url = "http://www.gravatar.com/" + email_hash
    return url


# private methods


def __get_email_hash(email_address):
    return hashlib.md5(email_address.strip().lower()).hexdigest()
