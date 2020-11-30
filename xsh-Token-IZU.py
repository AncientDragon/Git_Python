#!/usr/bin/env python

# @Author: Python
# @Date:   2016-09-20 16:45:33
# @Last Modified by:   Python
# @Last Modified time: 2016-09-20 16:54:56

import re
import onetimepass as otp


####Get IP
def IP_FIN(ip):
	IP_Mid = str(abs(int(ip[0])))
	for i in range(1, 4):
		IP_Mid = (IP_Mid+'.'+str(abs(int(ip[i]))))
	return IP_Mid

def Main():
	###get GoogleToken
	import onetimepass as otp
	my_secret = 'KZS774YENHNW2SVU'
	my_token=""
	my_token1 = otp.get_totp(my_secret)
	if len(str(my_token1)) == 6:
		my_token=my_token1
		###get IP addr
		IP_ORI = re.findall(r"\d+", str(xsh.Session.Path.split('\\')[-1]))
		IP = IP_FIN(IP_ORI)
		#result = xsh.Screen.WaitForString('OpenSSH\home\mr_ac>')
		#xsh.Screen.Send('ssh -i D:\PyCharm\Git_OPS\liuchenggong-jumpserver.pem liuchenggong@jumper.izuche.com -p 2222\r')
		result = xsh.Screen.WaitForString('Please enter 6 digits')
		xsh.Screen.Send(str(my_token)+'\r')
		result = xsh.Screen.WaitForString('Opt>')
		xsh.Session.Sleep(100)
		xsh.Screen.Send(str(IP)+'\r')
		xsh.Session.Sleep(100)
		xsh.Screen.Send('\r')

		xsh.Session.Sleep(100)
		result = xsh.Screen.WaitForString(' ~]$ ')
		#xsh.Screen.Send('sudo su -\rsu - dig\r')
		#xsh.Session.Sleep(100)
		#result = xsh.Screen.WaitForString(' ~]$ ')
		xsh.Screen.Clear()
