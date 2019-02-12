#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Author: Python
# @Date:   2016-11-13 00:15:32
# @Last Modified by:   Python
# @Last Modified time: 2016-11-13 01:16:12

import commands
import requests
import json

#ubuntu获取ip地址命令
ip = commands.getoutput("ip addr | grep inet | grep 24 | awk '{print $2}'| awk -F'/' '{print $1}'")

api_ip = ip
#centos6|centos7获取ip地址命令
#ip = commands.getoutput("/sbin/ip a| /bin/grep 'inet'| /bin/grep -vE '127.0.0.1|::'|/bin/awk '{print $2}'|grep -v '/32'|/bin/awk -F'/' '{print $1}'|/usr/bin/head -1")

#获取本机正在使用端口
port_dict = {}
port_message = commands.getoutput("netstat -tulnp | grep -v connections |grep -v 'Local Address' | awk '{print $4,$7}'")
port_message_list = port_message.split("\n")
for line in port_message_list:
    if len(line.split()) > 1:
        port_key = line.split()[0].split(":")[-1]
        port_dict[port_key] = line.split()[1]

#获取本机正在使用进程
process_dict = {}
process_message = commands.getoutput("ps -ef | awk '{print $2,$8}'| grep -v grep | egrep 'nginx|java|tomcat|redis|mysql|mongo|oracle|dubbo|rocketmq|zookeeper|kafka|flume|haproxy|elasticsearch|rabbitmq'")
process_message_list = process_message.split("\n")
for line in process_message_list:
    process_dict[line.split()[0]] =  line.split()[1]
#组织数据
send_data = {"ip":ip}
send_data["port"] = json.dumps(port_dict)
send_data["process"] = json.dumps(process_dict)
print send_data
#数据推送
url = "http://%s:9090/scan_port_process/" %api_ip
result = requests.post(url, data=send_data)
