#-*- coding:utf-8 -*-

n = input()

for i in range(n):
    line = list(raw_input())
    code = [x == '1' for x in line]
    syndrome = [0, 0, 0]

    syndrome[2] = code[0] ^ code[2] ^ code[4] ^ code[6]
    syndrome[1] = code[1] ^ code[2] ^ code[5] ^ code[6]
    syndrome[0] = code[3] ^ code[4] ^ code[5] ^ code[6]

    code_int = [c and 1 or 0 for c in code]

    if True in syndrome:
        syndrome = [s and 1 or 0 for s in syndrome]
        v = 0
        v += syndrome[0]*4 + syndrome[1]*2 + syndrome[2]

        if code_int[v-1]:
            code_int[v-1] = 0
        else:
            code_int[v-1] = 1

    print '%s%s%s%s' % (code_int[2], code_int[4], code_int[5], code_int[6])

# 문제 출처: https://algospot.com/judge/problem/read/HAMMINGCODE
