#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Author: Python
# @Date:   2016-09-11 02:54:26
# @Last Modified by:   Python
# @Last Modified time: 2016-09-22 16:15:34

import difflib

text1 = """
    text1: #define String1撒地方
    This module provides classes and functions for comparing sequences.
    including HTML and context and unified diffs.
    difflib document v7.4
    士大夫撒旦
    add 

"""
text1_lines = text1.splitlines ( )

text2 = """
    text2: #define String2
    This module provides classes and functions for Comparing sequences.
    including HTML and context and unified diffs.
    difflib document v7.5"""
text2_lines = text2.splitlines ( )

d = difflib.Differ ( )
diff = d.compare ( text1_lines , text2_lines )
print '\n'.join ( list ( diff ) )
