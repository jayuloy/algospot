#-*- coding:utf-8 -*-

import sys
n = int(sys.stdin.readline())

for i in range(n):
    line = sys.stdin.readline().rstrip('\n')
    even = [line[k] for k in range(0, len(line), 2)]
    odd = [line[k] for k in range(1, len(line), 2)]
    s = even + odd

    sys.stdout.write('%s\n' % ''.join(s))

# 문제 출처: https://algospot.com/judge/problem/read/ENCRYPT