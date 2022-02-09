import sys

sys.stdin=open('../data/get_decimal.txt', 'r')

n = int(input())

# 내 풀이
# decimal_count = 0
# for i in range(2, n+1):
#     cnt = 0
#     for j in range(1, i+1):
        
#         if i % j == 0:
#             # print(i, j)
#             cnt += 1
#     # print('소수 갯수:', cnt)
#     if cnt < 3:
#         decimal_count += 1

# print(decimal_count)

# 강의 풀이 : 에라토스테네스의 체 풀이 활용 / 배수의 성질을 이용해서 불 필요한 계산을 줄이는 연산법

ch = [0] * (n+1)
cnt = 0

for i in range(2, n+1):
    if ch[i] == 0:
        cnt+=1
        for j in range(i, n+1, i):
            ch[j] = 1

print(cnt)