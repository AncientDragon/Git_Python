#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time    : 6/19/2018 11:52 AM
# @Author  : Apy
# @File    : Python-Jenkins-run-job.py

import jenkins
import time
import sys


def run():
    server = jenkins.Jenkins("jenkins.gmfclou.com", username="liuchenggong", password="As111111")
    server.build_job("P2P-T2_gmjr-mmlc-p2p-static",parameters=None, token=None)
    while True:
        time.sleep(1)
        print 'check running job...'
        if len(server.get_running_builds()) == 0:
            break
        else:
            time.sleep(20)
    last_build_number = server.get_job_info("P2P-T2_gmjr-mmlc-p2p-static")['lastCompletedBuild']['number']
    build_info = server.get_build_info("P2P-T2_gmjr-mmlc-p2p-static", last_build_number)
    build_result = build_info['result']
    print 'Build result is ' + build_result
    if build_result == 'SUCCESS':
        sys.exit(0)
    else:
        sys.exit(-1)


if __name__ == '__main__':
    run()