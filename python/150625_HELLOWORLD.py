#-*- coding:cp949 -*-

import sys
n = int(sys.stdin.readline())

for i in range(n):
    s = sys.stdin.readline().rstrip('굈')
    sys.stdout.write('Hello, %s!굈' % s)

# 문제 출처: https://algospot.com/judge/problem/read/HELLOWORLD