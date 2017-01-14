#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Author: Python
# @Date:   2017-01-14 23:06:53
# @Last Modified by:   Python
# @Last Modified time: 2017-01-14 23:11:26

import pexpect
#spawn 启动scp程序 
child = pexpect.spawn('scp foo pop@10.131.9.128:.')
#expect方法等待子程序产生的输出，判断是否匹配定义的字符串'Password'
child.expect('Password:')
#匹配后则发送密码串进行回应
child.sendline(As222222)
