# uncompyle6 version 3.2.5
# Python bytecode 3.6 (3379)
# Decompiled from: Python 3.7.0 (default, Jan 20 2019, 13:20:46) 
# [Clang 10.0.0 (clang-1000.11.45.5)]
# Embedded file name: check.py
# Compiled at: 2019-03-03 14:04:26
# Size of source mod 2**32: 2058 bytes
"""
Created on Fri Mar  1 20:30:54 2019

@author: Sunanda
"""
import argparse
parser = argparse.ArgumentParser(description='The purpose of this application is to check \n                        the COMP 472/6721 Winter 2019 Projects')
parser.add_argument('-c', required=False,
  action='store_true',
  help='optional argument to check the format')
parser.add_argument('-m', required=False,
  action='store_true',
  help='check the trace files for minimax implementation')
parser.add_argument('-a', required=False,
  action='store_true',
  help='check the trace files for alpha beta implementation')
parser.add_argument('-f', dest='filename', required=True, help='output file from demos',
  metavar='FILE',
  type=argparse.FileType('r', encoding='UTF-8'))
args = parser.parse_args()
content = args.filename.read().strip()
groups = content.split('\n\n')
if args.m or args.a:
    print('\n\x1b[1;31;mACESS DENIED\x1b[0m ')
else:
    print('Checking format')
    error = 0
    traceNo = 0
    for i, bunch in enumerate(groups, 1):
        rows = bunch.split('\n')
        if i % 2 == 1:
            traceNo += 1
            if len(rows) != 2:
                error = 1
                break
        for val in rows:
            try:
                float(val)
            except:
                error = 2
                break

        if error != 0:
            break

    if error == 1:
        print('\n\x1b[1;31;mERROR:\x1b[0m To many values in the beginning (Trace No. ' + str(traceNo) + ')')
    else:
        if error == 2:
            print('\n\x1b[1;31;mERROR:\x1b[0m Number expected (Trace No. ' + str(traceNo) + ')')
        else:
            print('\n\x1b[1;32;mCORRECT FORMAT\x1b[0m')