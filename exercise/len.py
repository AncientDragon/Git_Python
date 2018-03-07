#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time    : 2/24/2018 10:03 AM
# @Author  : Apy
# @File    : len.py

# a = 1234
# b = "adsf234"
#
#
# print len(str(a))
# print len(b)

c = "C:\Users\Apy\Documents\NetSarang\Xshell\Sessions\Mylc-1\aa10.150.20.1-UE-nginx-ftp.xsh"

# IP = re.findall(r"\d+", c)
#for i in range(0, 7):
#    print(i)
#    print('.')
#print(i)
#print('\r')

import re
import onetimepass as otp
#my_secret = 'ZYPRDAEJVPBMFGUA'
#my_token = otp.get_totp(my_secret)
## print "my_token is %s"%my_token
#
#if len(str(my_token)) == 6:
#    fin_token = my_token
#else:
#    fin_token = "0" + str(my_token)
#xsh.Screen.Send(fin_token)
####enter token
#xsh.Screen.Send('\r')
IP = re.findall(r'\d+.\d+.\d+.\d+', c)
a=IP[0]
#IP = re.compile(r'(?<![\.\d])(?:\d{1,3}\.){3}\d{1,3}(?![\.\d])')
print IP
print a