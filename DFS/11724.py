# 백준 11724 연결 요소의 개수

import sys

input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[0]* N for _ in range(N)]

for _ in range(M):
    x, y = map(lambda x: x-1, map(int, input().split()))
    graph[x][y] = graph[y][x] = 1

visited = [False] * N
cnt = 0

def dfs(now):
    for i in range(N):
        if graph[now][i] and not visited[i]:
            visited[i] = True
            dfs(i) 

for i in range(N):
    if not visited[i]:
        cnt += 1
        visited[i] = True
        dfs(i)


print(cnt)

