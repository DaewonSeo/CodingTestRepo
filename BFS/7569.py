# 백준 7569 토마토
from collections import deque
import sys

input = sys.stdin.readline

M, N, H = map(int, input().split())
graph = [ [ list(map(int, input().split())) for _ in range(N)]for _ in range(H) ]

# visited = [ [ [False] * M for _ in range(N) ] for _ in range(H) ]
dz = (0, 0, 0, 0, -1, 1)
dx = (1, -1, 0, 0, 0, 0)
dy = (0, 0, -1, 1, 0, 0)

def is_valid_coord(z, x, y):
    return 0 <= z < H and 0 <= x < N and 0 <= y < M

def bfs():
    # visited[z][y][x] = True
    while dq:
        z, x, y = dq.popleft()

        for k in range(6):
            nz = z + dz[k]
            nx = x + dx[k]
            ny = y + dy[k]

            if is_valid_coord(nz, nx, ny) and graph[nz][nx][ny] == 0:
                graph[nz][nx][ny] = graph[z][x][y] + 1
                dq.append((nz, nx, ny))

dq = deque()
for i in range(H):
    for j in range(N):
        for k in range(M):
            if graph[i][j][k] == 1:
                dq.append((i, j, k))


bfs()

z = 1
result = - 1
for i in range(H):
    for j in range(N):
        for k in range(M):
            if graph[i][j][k] == 0:
                z = 0
            result=max(result, graph[i][j][k])

if z == 0:
    print(-1)
elif result == 1:
    print(0)

else:
    print(result-1)
