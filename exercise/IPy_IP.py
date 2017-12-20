#!/usr/bin/env python
# coding=utf-8

from IPy import IP

# import IPy.IP
ip = IP('192.168.44.0/24')
print ip.len()
for x in ip:
    print (x)
