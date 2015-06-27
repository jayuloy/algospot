#-*- coding:utf-8 -*-

n = input()

for i in range(n):
    value = 0
    total = int(input())
    line = raw_input().split()

    for v in line:
        value += int(v)

    if value <= total:
        print 'YES'
    else:
        print 'NO'

# 문제 출처: https://algospot.com/judge/problem/read/HOTSUMMER