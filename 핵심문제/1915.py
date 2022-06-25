#백준 1915번 문제 가장 큰 정사각형

# from collections import deque
import sys

input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

graph = [ list(map(int, input().rstrip())) for _ in range(N)]
dp = [[0] * M for _ in range(N)]

# 완전탐색을 하면 시간초과가 발생하기 때문데 다른 방법을 사용해야 한다.
# DP를 사용해서 점화식으로 해결한다.

for i in range(M):
    if graph[0][i]:
        dp[0][i] = 1

for i in range(1, N):
    if graph[i][0]:
        dp[i][0] = 1

    for j in range(1, M):
        if graph[i][j]:
            dp[i][j] = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1]) + 1

ans = 0
for i in range(N):
    for j in range(M):
        ans = max(ans, dp[i][j])

print(ans ** 2)

