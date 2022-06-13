# 백준 2748번 문제 피보나치 수 2
import sys

input = sys.stdin.readline

N = int(input().rstrip())

L = [0] * (N+1)
L[0] = 0
L[1] = 1
for i in range(2, N+1):
    L[i] = L[i-1] + L[i-2]

print(L[-1]) 