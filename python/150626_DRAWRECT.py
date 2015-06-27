#-*- coding:utf-8 -*-

import sys
n = int(sys.stdin.readline())

for i in range(n):
    x = []
    y = []

    for j in range(3):
        line = sys.stdin.readline().rstrip('\n').split()
        x.append(line[0])
        y.append(line[1])

    sx = [item for item in x if x.count(item) == 1]
    sy = [item for item in y if y.count(item) == 1]
    sys.stdout.write('%s %s\n' % (sx[0], sy[0]))

# 문제 출처: https://algospot.com/judge/problem/read/DRAWRECT