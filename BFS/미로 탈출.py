# 이것이 코딩테스트다 2021 미로 탈출 문제

from collections import deque
import sys

input = sys.stdin.readline

N, M = map(int, input().split())

graph = [ list(map(int, input().rstrip())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    dq = deque()
    dq.append((x, y))
    
    while dq:
        x, y = dq.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue

            if graph[nx][ny] == 0:
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                dq.append((nx, ny))


    return graph[N-1][M-1]


print(bfs(0, 0))


    