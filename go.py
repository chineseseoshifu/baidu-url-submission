# -*- coding: utf-8 -*-

import requests

seed_file = open('seed.txt', 'r')
urllist = '\n'.join(seed_file.readlines())

# Your Baidu request URL, looking like http://data.zz.baidu.com/urls?site=www.a.com&token=YOUR-PRIVATE-TOKEN
baidu_request_url = "INSERT YOUR REQUEST URL HERE"

r = requests.post(
    baidu_request_url,
    data=urllist,
    headers={'content-type':'text/plain'})

print r.text