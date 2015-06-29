#-*- coding:utf-8 -*-
from itertools import combinations

def GenDiv(number):
    factor_list = [1]
    sqroot = int(number**0.5)

    for factor in xrange(2, sqroot+1):
        if number % factor == 0:
            factor_list.append(factor)
            if not factor == number/factor:
                factor_list.append(number/factor)

    return sorted(factor_list)

n = input()

for i in range(n):
    num = input()

    divisors = GenDiv(num)
    total = sum(divisors)
    check = False
    subtotal = 0
    sub_div = []

    if not total > num:
        print 'not weird'
    else:
        subtotal = total - num
        sub_div = [m for m in divisors if m <= subtotal]

        for l in xrange(len(sub_div)+1, 1, -1):
            for subset in combinations(sub_div, l):
                if sum(subset) == subtotal:
                    print 'not weird'
                    check = True
                    break
            if check:
                break
        else:
            print 'weird'

# 문제 출처: https://algospot.com/judge/problem/read/WEIRD

# 1. 먼저 num의 약수를 크기가 작은 순으로 리스트에 정렬시킨다.
# 2. 리스트 내의 모든 수를 더한 값(total)이 num보다 크면 total에서 num을 뺀다.(subtotal)
# 3. 약수들 중에 subtotal 이하인 약수들을 구한다. (sub_div)
# 4. sub_div의 조합 중 합이 subtotal과 같으면 not weird, 다르면 weird 이다.

# 참고: https://algospot.com/forum/read/1942/#c9233