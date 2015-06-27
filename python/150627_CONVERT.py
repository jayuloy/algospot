#-*- coding:utf-8 -*-

n = input()

for i in range(n):
    line = raw_input().split()
    value = float(line[0])
    unit = line[1]
    if unit == 'kg':
        c_value = value * 2.2046
        c_unit = 'lb'
    elif unit == 'lb':
        c_value = value * 0.4536
        c_unit = 'kg'
    elif unit == 'l':
        c_value = value * 0.2642
        c_unit = 'g'
    elif unit == 'g':
        c_value = value * 3.7854
        c_unit = 'l'

    print '%s %.4f %s' % (i+1, round(c_value, 4), c_unit)

# 문제 출처: https://algospot.com/judge/problem/read/CONVERT