#-*- coding:utf-8 -*-
import string

n = input()

for i in range(n):
    line = raw_input()

    s = string.replace(line, '%20', ' ')
    s = string.replace(s, '%21', '!')
    s = string.replace(s, '%24', '$')
    s = string.replace(s, '%28', '(')
    s = string.replace(s, '%29', ')')
    s = string.replace(s, '%2a', '*')
    s = string.replace(s, '%25', '%')

    print '%s' % s

# 문제 출처: https://algospot.com/judge/problem/read/URI