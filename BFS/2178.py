# 백준 2178번 미로탈출

from collections import deque
import sys

input = sys.stdin.readline

N, M = map(int, input().split())

graph = []
for i in range(N):
    graph.append(list(map(int, input().rstrip())))


dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

checked = [ [False] * M for _ in range(N)]


def is_valid_coord(y, x):
    return 0<= y < N and 0 <= x < M

def bfs():
    dq = deque()
    dq.append((0, 0, 1))
    checked[0][0] = True

    while dq:
        y, x, cnt = dq.popleft()
        
        if y == N - 1 and x == M - 1:
            return cnt
        
        cnt = cnt + 1

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            
            if is_valid_coord(ny, nx) and graph[ny][nx] == 1 and not checked[ny][nx]:
                checked[ny][nx] = True
                dq.append((ny, nx, cnt))


print(bfs())
    