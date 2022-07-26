import sys

input = sys.stdin.readline
n = int(input())

DP = [0] * 1000005

DP[1] = 0

for i in range(2, n+1):
    DP[i] = DP[i-1] + 1
    if i % 2 == 0:
        DP[i] = min(DP[i], DP[i//2] + 1)

    if i % 3 == 0:
        DP[i] = min(DP[i], DP[i//3] + 1)



print(DP[n])

