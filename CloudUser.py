# coding=utf-8
import json
import time


class _Signature(object):
    string_template = 'CloudUser.Signature[token=%(token)s,appKey=%(appKey)s,nonce=%(nonce)s,timestamp=%(timestamp)s]'

    def __init__(self, sign_dict):
        self.token = sign_dict.get('token', None)
        self.appKey = sign_dict.get('appKey', None)
        self.nonce = sign_dict.get('nonce', None)
        self.timestamp = sign_dict.get('timestamp', time.time())
        self.check = sign_dict.get('check', None)

    def __unicode__(self):
        value_dict = {
            'token': self.token if self.token is not None else '<null>',
            'appKey': self.appKey if self.appKey is not None else '<null>',
            'nonce': self.nonce if self.nonce is not None else '<null>',
            'timestamp': self.timestamp if self.timestamp is not None else '<null>',
        }
        return self.string_template % value_dict

    def __str__(self):
        return self.__unicode__().encode('utf-8')


class _Item(object):
    string_template = 'CloudUser.Item[code=%(code)s,name=%(name)s]'

    def __init__(self, item_dict):
        self.code = item_dict.get('code', None)
        self.name = item_dict.get('name', None)

    def __unicode__(self):
        value_dict = {
            'code': self.code if self.code is not None else '<null>',
            'name': self.name if self.name is not None else '<null>'
        }
        return self.string_template % value_dict

    def __str__(self):
        return self.__unicode__().encode('utf-8')


class _File(object):
    string_template = 'CloudUser.File[id=%(id)s,url=%(url)s]'

    def __init__(self, item_dict):
        self.id = item_dict.get('id', None)
        self.url = item_dict.get('url', None)

    def __unicode__(self):
        value_dict = {
            'id': self.id if self.id is not None else '<null>',
            'url': self.url if self.url is not None else '<null>'
        }
        return self.string_template % value_dict

    def __str__(self):
        return self.__unicode__().encode('utf-8')


class CloudUser(object):
    string_template = 'CloudUser[idsNo=%(idsNo)s,nickName=%(nickName)s,realName=%(realName)s,avatar=%(avatar)s,gender=%(gender)s,enterYear=%(enterYear)s,birthday=%(birthday)s,region=%(region)s,dept=%(dept)s,major=%(major)s,qq=%(qq)s,sign=%(sign)s]'

    def __init__(self, json_string):
        data_dict = json.loads(json_string)

        self.idsNo = data_dict.get('idsNo', None)
        self.nickName = data_dict.get('nickName', None)
        self.realName = data_dict.get('realName', None)
        self.avatar = _File(data_dict.get('avatar')) if data_dict.get('avatar', None) is not None else None
        self.gender = data_dict.get('gender', None)
        self.enterYear = data_dict.get('enterYear', None)
        self.birthday = data_dict.get('birthday', None)
        self.region = _Item(data_dict.get('region')) if data_dict.get('region', None) is not None else None
        self.dept = _Item(data_dict.get('dept')) if data_dict.get('dept', None) is not None else None
        self.major = _Item(data_dict.get('major')) if data_dict.get('major', None) is not None else None
        self.qq = data_dict.get('qq', None)
        self.sign = _Signature(data_dict.get('sign')) if data_dict.get('sign', None) is not None else None

    def __unicode__(self):
        value_dict = {
            'idsNo': self.idsNo if self.idsNo is not None else '<null>',
            'nickName': self.nickName if self.nickName is not None else '<null>',
            'realName': self.realName if self.realName is not None else '<null>',
            'avatar': self.avatar if self.avatar is not None else '<null>',
            'gender': self.gender if self.gender is not None else '<null>',
            'enterYear': self.enterYear if self.enterYear is not None else '<null>',
            'birthday': self.birthday if self.birthday is not None else '<null>',
            'region': self.region if self.region is not None else '<null>',
            'dept': self.dept if self.dept is not None else '<null>',
            'major': self.major if self.major is not None else '<null>',
            'qq': self.qq if self.qq is not None else '<null>',
            'sign': self.sign if self.sign is not None else '<null>',
        }
        return self.string_template % value_dict

    def __str__(self):
        return self.__unicode__().encode('utf-8')
