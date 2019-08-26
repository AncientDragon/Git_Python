#!/usr/bin/env python

# @Author: Python
# @Date:   2016-09-20 16:45:33
# @Last Modified by:   Python
# @Last Modified time: 2016-09-20 16:54:56

import hmac,base64,struct,hashlib,time,re,sys

def Token(secretKey):
    input = int(time.time())//30
    key = base64.b32decode(secretKey)
    msg = struct.pack(">Q", input)
    googleCode = hmac.new(key, msg, hashlib.sha1).digest()
    o = ord(googleCode[19]) & 15
    googleCode = str((struct.unpack(">I", googleCode[o:o+4])[0] & 0x7fffffff) % 1000000)
    if len(googleCode) == 5:             # 如果验证码的第一位是0，则不会显示。此处判断若是5位码，则在第一位补上0
        googleCode = '0' + googleCode
    return googleCode

#def get_hotp_token(secret, intervals_no):
#	key = base64.b32decode(secret, True)
#	msg = struct.pack(">Q", intervals_no)
#	h = hmac.new(key, msg, hashlib.sha1).digest()
#	o = ord(h[19]) & 15
#	h = (struct.unpack(">I", h[o:o+4])[0] & 0x7fffffff) % 1000000
#	return h

#def get_totp_token(secret):
#	return get_hotp_token(secret, intervals_no=int(time.time())//30)

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
	my_token = str(Token(my_secret))
	###get IP addr
	IP_ORI = re.findall(r"\d+", str(xsh.Session.Path.split('\\')[-1]))
	###enter ip addr
	#for i in range(0, 3):
	#	xsh.Screen.Send(str(abs(int(IP[i])))+'.')
	#xsh.Screen.Send(str(abs(int(IP[3])))+'\r')
	IP = IP_FIN(IP_ORI)
	#xsh.Session.Sleep(1000)
	result = xsh.Screen.WaitForString('OpenSSH\home\mr_ac>')
	xsh.Screen.Send('ssh -i D:\PyCharm\Git_OPS\liuchenggong-jumpserver.pem liuchenggong@jumper.izuche.com -p 2222\r')
	result = xsh.Screen.WaitForString('Please enter 6 digits')
	xsh.Screen.Send(my_token+'\r')
	result = xsh.Screen.WaitForString('Opt>')
	xsh.Screen.Send(str(IP)+'\r')
	result = xsh.Screen.WaitForString(' ~]$ ')
	xsh.Screen.Send('sudo su -\rsu - dig\r')
	xsh.Screen.Clear()