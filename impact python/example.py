#-*- coding:utf-8 -*-

import requests
import time
import string

URL = "http://172.16.3.67:8080/cardread?user_id=flag"
print(URL)
requests.get(URL)
print("[+] success")
