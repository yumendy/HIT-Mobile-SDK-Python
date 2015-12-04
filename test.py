from CloudUser import CloudUser
from CloudUtils import check

from key import app_secret


def test():
    with open('test.json') as fp:
        json_string = fp.read()
    cu = CloudUser(json_string)
    print cu
    print check(cu, app_secret)


if __name__ == '__main__':
    test()
