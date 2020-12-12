import bs4 as bs
import urllib.request
import time
import random
import string
import requests
import json
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re
from fake_useragent import UserAgent

# # Generating a proxy
# def get_proxies(ua):
#     proxies = []
#     proxies_req = Request('https://www.sslproxies.org/')
#     proxies_req.add_header('User-Agent', ua.random)
#     proxies_doc = urlopen(proxies_req).read().decode('utf8')
#
#     soup = BeautifulSoup(proxies_doc, 'html.parser')
#     proxies_table = soup.find(id='proxylisttable')
#
#   # Save proxies in the array
#     for row in proxies_table.tbody.find_all('tr'):
#         proxies.append({
#                         'ip':   row.find_all('td')[0].string,
#                         'port': row.find_all('td')[1].string})
#     return proxies
#
# def random_proxy(proxies):
#   return random.choice(proxies)
#
#
# def fixaccount():
#     print('sending the information to the sign up page')
#     url = 'http://whatismyipaddress.com/fr/mon-ip'
#     headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0'}
#     r = requests.get(url, headers=headers, proxies=proxyf)
#     print(r.text)
#     time.sleep(7)
#
#
# ua = UserAgent()
# proxies = get_proxies(ua)
# nproxy = random_proxy(proxies)
#
# prostr = str(nproxy)
# ip = prostr.split(',')[0]
# port = prostr.split(',')[1]
# ipa = ip.split(':')[1]
# porta = port.split(':')[1]
# fport = porta.replace('}', '')
#
# ips = ipa.replace("'", "")
# ports = fport.replace("'", "")
# pip = ips.replace(" ", "")
# pport = ports.replace(" ", "")
#
#
# proxy = {
#  "http": "http://%s:%s"%(pip, pport),
#  "https": "http://%s:%s"%(pip, pport),
# }
#
# proxyf = {
#  "http": "http://vnpfwklm-rotate:kz65gib69zcm@45.9.123.41:80",
#  "https": "http://vnpfwklm-rotate:kz65gib69zcm@45.9.123.41:80",
# }
#
# print(proxy)
#
# fixaccount()

#
# import random
# import string
#
#
# def get_random_deviceid(length):
#     alphanumiric = string.ascii_lowercase + string.digits
#     result_str = ''.join(random.choice(alphanumiric) for i in range(length))
#     return result_str
#
#
# randDeviceID = get_random_deviceid(16)
# print(randDeviceID)

inputFile = open('50ACC.txt', 'r')
exportFile = open('2-50gglacc.txt', 'w')
for line in inputFile:
   new_line = line.replace('\t', ':')
   exportFile.write(new_line)

inputFile.close()
exportFile.close()