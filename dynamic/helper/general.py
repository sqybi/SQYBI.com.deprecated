import urllib

import helper.constants


def get_alert_level(request):
    if "alertlevel" in request.GET:
        return helper.constants.ALERT_LEVELS[request.GET["alertlevel"]]
    else:
        return helper.constants.alert_level


def get_alert_message(request):
    if "alertmsg" in request.GET:
        return request.GET["alertmsg"]
    else:
        return helper.constants.alert_message


def get_redirect_url(base_url, parameters):
    first_arg = True
    if '?' in base_url:
        first_arg = False

    for parameter in parameters:
        if first_arg:
            base_url += '?'
        else:
            base_url += '&'

        base_url += urllib.quote_plus(parameter["key"]) + '=' + urllib.quote_plus(parameter["value"])

        first_arg = False