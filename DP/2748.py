# 백준 2748번 문제 피보나치 수 2
import sys

input = sys.stdin.readline

# 반복문
# N = int(input().rstrip())

# L = [0] * (N+1)
# L[0] = 0
# L[1] = 1
# for i in range(2, N+1):
#     L[i] = L[i-1] + L[i-2]

# print(L[-1]) 

# 재귀
cache = [-1] * 91
cache[0] = 0
cache[1] = 1

def f(n):
    if cache[n] == -1:
        cache[n] = f(n-1) + f(n-2)

    return cache[n]

print(f(int(input()))) 