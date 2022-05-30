#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022-05-30 15:26
# @Author  : van long
# @File    : ql
# @Software: IntelliJ IDEA
import json
import os
import time

import requests

class Ql(object):

    prefix = 'http://127.0.0.1:5700'

    def get_token(self):
        file_path = '/ql/data/config/auth.json'
        if not os.path.lexists(file_path):
            file_path = 'auth.json'

        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)['token']

    def get_envs(self):
        token = self.get_token()
        params = {
            'searchValue': 'JD_COOKIE',
            't': time.time()
        }
        headers = {
            'Accept': 'application/json',
            'authorization': 'Bearer {0}'.format(token),
        }
        resp = requests.get(self.prefix + '/api/envs', params, headers=headers)
        return resp.json()

    def add_env(self):
        pass

    def update_env(self):
        pass

    def del_env(self):
        pass

if __name__ == '__main__':
    ql = Ql()
    print(ql.get_envs())