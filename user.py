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
        self.pt_key = re.search('pt_key=(.*?);', cookie).group(1)
        self.pt_pin = re.search('pt_pin=(.*?);', cookie).group(1)
        self.cookie = 'pt_key=' + self.pt_key + ';pt_pin=' + urllib.parse.quote(self.pt_pin) + ';'
        self.remarks = self.pt_pin

    def ck_login(self):
        envs = ql.get_envs()

        env = filter(lambda x: re.search('pt_pin=(.*?);', x['value']).group(1) == urllib.parse.quote(self.pt_pin), envs)
        find_env = list(env)
        if find_env:
            env = find_env[0]
            response = ql.update_env(env['id'], remarks=self.remarks, cookie=self.cookie)
            message = '欢迎回来' + self.remarks if response['code'] == 200 else '更新账户错误，请检查Cookie后重试！！！'
        else:
            response = ql.add_env(cookie=self.cookie, remarks=self.remarks)
            message = '注册成功' + self.remarks if response['code'] == 200 else '添加账户错误，请检查Cookie后重试！！！'
        return message


