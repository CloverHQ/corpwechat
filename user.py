#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022-05-30 15:56
# @Author  : van long
# @File    : user
# @Software: IntelliJ IDEA
import re
import urllib.parse

from ql import Ql

ql = Ql()


class User(object):

    def __init__(self, cookie):
        self.pt_key = re.search('pt_key=(.*?);', cookie).group()
        self.pt_pin = re.search('pt_key=(.*?);', cookie).group()
        self.cookie = 'pt_key=' + self.pt_key + ';pt_pin=' + self.pt_pin + ';'
        self.remarks = urllib.parse.quote(self.pt_pin)

    def ck_login(self):
        envs = ql.get_envs()

        for env in envs:
            if re.search('pt_pin=(.*?);', env['value']).group() == self.pt_pin:
                response = ql.update_env(env['eid'], remarks=self.remarks, cookie=self.cookie)
                message = response['code'] == 200 if '欢迎回来' else '更新账户错误，请检查Cookie后重试！！！'
            else:
                response = ql.add_env(cookie=self.cookie, remarks=self.remarks)
                message = response['code'] == 200 if '注册成功' else '添加账户错误，请检查Cookie后重试！！！'
            return message

