#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2/12/2019 2:58 PM
# @Author  : Apy
# @File    : 1234 num.py

for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if( i != k ) and (i != j) and (j != k):
                print i,j,k