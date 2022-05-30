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
        if not os.path.exists(file_path):
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
        return resp.json()['data']

    def add_env(self, cookie, remarks):
        token = self.get_token()
        params = {
            't': time.time()
        }

        data = {
            'name': 'JD_COOKIE',
            'value': cookie,
            'remarks': remarks
        }

        headers = {
            'Accept': 'application/json',
            'authorization': 'Bearer {0}'.format(token),
            'Content-Type': 'application/json;charset=UTF-8'
        }
        resp = requests.post(self.prefix + '/api/envs', params=params, json=[data], headers=headers)
        return resp.json()

    def update_env(self, eid, remarks, cookie):
        token = self.get_token()
        params = {
            't': time.time()
        }

        data = {
            'name': 'JD_COOKIE',
            'value': cookie,
            'id': eid,
            'remarks': remarks
        }

        headers = {
            'Accept': 'application/json',
            'authorization': 'Bearer {0}'.format(token),
            'Content-Type': 'application/json;charset=UTF-8',
            'Content-Length': str(len(json.dumps(data)))
        }
        resp = requests.put(self.prefix + '/api/envs', params=params, json=data, headers=headers)
        return resp.json()

    def del_env(self, eid):
        token = self.get_token()
        params = {
            't': time.time()
        }

        headers = {
            'Accept': 'application/json',
            'authorization': 'Bearer {0}'.format(token),
            'Content-Type': 'application/json;charset=UTF-8',
        }
        resp = requests.delete(self.prefix + '/api/envs', params=params, headers=headers, json=[eid])
        return resp.json()


if __name__ == '__main__':
        json = '{"123":123}'
        print(json['123'])
