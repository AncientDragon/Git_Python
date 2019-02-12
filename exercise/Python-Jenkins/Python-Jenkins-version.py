#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time    : 6/19/2018 11:52 AM
# @Author  : Apy
# @File    : Python-Jenkins-version.py

import sys
import jenkins

job_name=sys.argv[1]
server = jenkins.Jenkins("http://jenkins.gmfcloud.com", username="liuchenggong", password="As111111")
user = server.get_whoami()
version = server.get_version()
print("Hello %s from Jenkins %s" % (user["fullName"], version))
job_info=server.get_job_info(job_name)
print ("%s" %job_info)
build_job=server.build_job(job_name)