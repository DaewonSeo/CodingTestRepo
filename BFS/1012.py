# 백준 유기농 배추 1012 문제

from collections import deque
import sys


def bfs(graph, a, b):
    dx = (-1, 1, 0, 0)
    dy = (0, 0, -1, 1)
    dq = deque()
    dq.append((a, b))
    graph[a][b] = 0

    while dq:
        x, y = dq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny < 0  or ny >= M:
                continue

            if graph[nx][ny] == 1:
                dq.append((nx, ny))
                graph[nx][ny] = 0


c = int(input())

for _ in range(c):
    cnt = 0
    N, M, K = map(int, input().split())

    graph = [ [0] * M for _ in range(N)]

    for _ in range(K):
        x, y = map(int, input().split())
        graph[x][y] = 1

    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                bfs(graph, i, j)
                cnt += 1
    print(cnt)


