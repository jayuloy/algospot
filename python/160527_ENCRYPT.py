n = int(input())

for i in range(n):
    s = input().strip()

    s1 = [k for index, k in enumerate(s) if index % 2 == 0]
    s2 = [k for index, k in enumerate(s) if index % 2]

    result = s1 + s2
    result = ''.join(result)

    print(result)

# ENCRYPT  windowlicker  47달 전 68B 47ms 정답
# 소스 코드
#
# for i in range(0,int(input())):
# 	s=input()
# 	print(s[0::2]+s[1::2])