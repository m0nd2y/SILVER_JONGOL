#-*- coding:utf-8 -*-

import requests
import time
import string

lenth = 0
URL = "http://172.16.3.67:8080/login?user_id="
def loop(line) :
    time.sleep(0.3)
    if not line:
        line = r.readline()
        loop(line)
tmp = 0
while(1) :
    r = open("flag.txt", mode='r')
    str = r.readlines()
    beforelenth = lenth
    lenth = len(str)
    print("[+]data len : ", lenth)
    time.sleep(0.1)
    if (beforelenth != lenth) :
        for i in range(tmp, lenth):
            time.sleep(0.2)
            print("[+]send data : ", str[i])
            URL += str[i].strip()
            URL += "&password=1234"
            tmp = i+1
            print("[+]send URL : ", URL)
            requests.get(URL)
            URL = "http://172.16.3.67:8080/login?user_id="

#url setting

#http://localhost:8080/cardread?user_id=

'''
#change to your own cookies
cookies = dict(PHPSESSID="")
response = requests.get(URL, cookies = cookies)
print (response.text)
'''
