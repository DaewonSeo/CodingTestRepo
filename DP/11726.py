# 백준 11726번 2xn 타일링 

import sys

input = sys.stdin.readline

N = int(input().rstrip())

cache = [0] * 1001

cache[1] = 1
cache[2] = 2
for i in range(3, 1001):
    cache[i] = cache[i-1] + cache[i-2]
    cache[i] %= 10007

print(cache[N])