#백준 11051문제 이항 계수 2

import sys

input = sys.stdin.readline

N, K = map(int, input().rstrip().split())

cache = [[0] * 1001 for _ in range(1001)]

# def bino(n, k):
#     if cache[n][k]:
#         return cache[n][k]
#     if k==0 or k == n:
#         cache[n][k] = 1
#     else:
#         cache[n][k] = bino(n-1, k-1) + bino(n-1, k)
#         cache[n][k] %= 10007

#     return cache[n][k]

# print(bino(N, K))

for i in range(1001):
    cache[i][0] = cache[i][i] = 1
    for j in range(1, i):
        cache[i][j] = cache[i-1][j-1] + cache[i-1][j]
        cache[i][j] %= 10007

print(cache[N][K])