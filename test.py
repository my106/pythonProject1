# -*- coding: UTF-8 -*-
# -*- name: my -*-
# -*- time: system -*-
import requests


def patch_ip_manage():
    requests.patch(
        url='http://127.0.0.1:5000/v1/'
    )