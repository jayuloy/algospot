#-*- coding:utf-8 -*-

def chartoint(value):
    c = 0

    if value == 'zero':
        c = 0
    elif value == 'one':
        c = 1
    elif value == 'two':
        c = 2
    elif value == 'three':
        c = 3
    elif value == 'four':
        c = 4
    elif value == 'five':
        c = 5
    elif value == 'six':
        c = 6
    elif value == 'seven':
        c = 7
    elif value == 'eight':
        c = 8
    elif value == 'nine':
        c = 9
    elif value == 'ten':
        c = 10

    return c

def checksol(x, c):
    if x == 0:
        s = 'zero'
    elif x == 1:
        s = 'one'
    elif x == 2:
        s = 'two'
    elif x == 3:
        s = 'three'
    elif x == 4:
        s = 'four'
    elif x == 5:
        s = 'five'
    elif x == 6:
        s = 'six'
    elif x == 7:
        s = 'seven'
    elif x == 8:
        s = 'eight'
    elif x == 9:
        s = 'nine'
    elif x == 10:
        s = 'ten'

    if not len(s) == len(c):
        return 'No'

    for j in s:
        if not s.count(j) == c.count(j):
            return 'No'

    return 'Yes'

n = input()

for i in range(n):
    line = raw_input().split()

    operand_a = line[0]
    operand_b = line[2]
    operator = line[1]
    solution = line[4]

    value_a = chartoint(operand_a)
    value_b = chartoint(operand_b)

    if operator == '+':
        sol = value_a + value_b
    elif operator == '-':
        sol = value_a - value_b
    elif operator == '*':
        sol = value_a * value_b

    if sol < 0 or sol > 10:
        print 'No'
    else:
        print checksol(sol, solution)

# 문제 출처: https://algospot.com/judge/problem/read/XHAENEUNG