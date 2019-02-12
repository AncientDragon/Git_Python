#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time    : 5/1/2018 2:38 PM
# @Author  : Apy
# @File    : Linux-monitor.py

from __future__ import print_function
from collections import OrderedDict
import pprint

def CPUinfo():
    '''
    Return the information in /proc/CPUinfo
    as a dictionary in the follown format:
    CPU_info['proc0']={...}
    CPU_info['proc0']={...}
    '''
    CPUinfo=OrderedDict()
    procinfo=OrderedDict()

    nprocs = 0
    with open('/proc/cpuinfo') as f:
        for line in f:
            if not line.strip():
                # end of one processor
                CPUinfo['procs%s' % nprocs] = procinfo
                nprocs += 1
                # Reset
                procinfo = OrderedDict()
            else:
                if len(line.split(':')) == 2:
                    procinfo[line.split(':')[0].strip()] = line.split(':')[1].strip()
                else:
                    procinfo[line.split(':')[0].strip()] = ''
    return CPUinfo
if __name__=='__main__':
    CPUinfo = CPUinfo()
    for processor in CPUinfo.keys():
        print(CPUinfo[processor]['model name'])