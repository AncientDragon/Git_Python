#!/usr/bin/env python

# @Author: Python
# @Date:   2016-09-20 16:45:33
# @Last Modified by:   Python
# @Last Modified time: 2016-09-20 16:54:56

import hmac,base64,struct,hashlib,time,re
import sys

def get_hotp_token(secret, intervals_no):
	key = base64.b32decode(secret, True)
	msg = struct.pack(">Q", intervals_no)
	h = hmac.new(key, msg, hashlib.sha1).digest()
	o = ord(h[19]) & 15
	h = (struct.unpack(">I", h[o:o+4])[0] & 0x7fffffff) % 1000000
	return h

def get_totp_token(secret):
	return get_hotp_token(secret, intervals_no=int(time.time())//30)
	
####获取IP形式字符串
#def IP_FIN(ip):
#   IP_Mid = str(abs(int(ip[0])))
#   for i in range(1, 4):
#       IP_Mid = (IP_Mid+'.'+str(abs(int(ip[i]))))
#   return IP_Mid	
def IP_FIN(ip):
	abs_ip = [int(i) for i in ip]
	IP_FIN = '.'.join(str(i)for i in abs_ip)
	return IP_FIN

def Main():	
	import onetimepass as otp
	my_secret = '3NXBYATWGIIZ3LEV'
	my_secret = 'KZS774YENHNW2SVU'
	my_token = str(get_totp_token(my_secret))
	xsh.Screen.Send(my_token+'\r')

	###get IP addr
	IP_ORI = re.findall(r"\d+", str(xsh.Session.Path.split('\\')[-1]))
	###enter ip addr
	#for i in range(0, 3):
	#	xsh.Screen.Send(str(abs(int(IP[i])))+'.')
	#xsh.Screen.Send(str(abs(int(IP[3])))+'\r')
	IP = IP_FIN(IP_ORI)
	xsh.Screen.Send(str(IP)+'\r')