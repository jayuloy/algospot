#-*- coding:utf-8 -*-

n = input()

for i in range(n):
    line = raw_input().split()
    k = int(line[0])
    s = line[1]
    if k > 1:
        s = s[:k-1] + s[k:]
    else:
        s = s[k:]

    print '%s %s' % (i+1, ''.join(s))

# 문제 출처: https://algospot.com/judge/problem/read/MISPELL