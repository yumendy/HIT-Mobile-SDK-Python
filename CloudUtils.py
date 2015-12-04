from hashlib import sha1


def _get_sign(cu, app_secret):
    return sha1(str(cu) + app_secret).hexdigest()


def check(cu, app_secret):
    return cu.sign.check == _get_sign(cu, app_secret)
