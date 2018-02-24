#!/usr/bin/env python

# @Author: Python
# @Date:   2016-09-20 16:45:33
# @Last Modified by:   Python
# @Last Modified time: 2016-09-20 16:54:56

import re


def Main():
    import onetimepass as otp
    my_secret = 'ZYPRDAEJVPBMFGUA'
    my_token = otp.get_totp(my_secret)
    # print "my_token is %s"%my_token

    if len(str(my_token)) == 6:
        fin_token = my_token
    else:
        fin_token = "0" + str(my_token)
    xsh.Screen.Send(fin_token)
    ###enter token
    xsh.Screen.Send('\r')
    IP = re.findall(r"\d+", str(xsh.Session.Path))

    ###enter ip addr
    for i in range(0,3):
        xsh.Screen.Send(IP[i])
        xsh.Screen.Send('.')
    xsh.Screen.Send(IP[3])
    xsh.Screen.Send('\r')
    ###sudo su
    xsh.Screen.Synchronous = True
    xsh.Session.Sleep(2500)
    xsh.Screen.Send("sudo su")
    xsh.Screen.Send('\r')