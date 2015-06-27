#-*- coding:utf-8 -*-

import sys
n = int(sys.stdin.readline())

for i in range(n):
    line = sys.stdin.readline().rstrip('\n')
    s = [line[k:k+2] for k in range(0, len(line), 2)]
    s.sort()

    sys.stdout.write('%s\n' % ''.join(s))

# 문제 출처: https://algospot.com/judge/problem/read/LECTURE