# 백준 7562번 나이트의 이동 문제

from collections import deque
import sys

input = sys.stdin.readline

dx = (-2, -1, 1, 2, 2, 1, -1, -2)
dy = (1, 2, 2, 1, -1, -2, -2, -1)


def is_valid_coord(x, y):
    return 0 <= x < I and 0 <= y < I
def bfs(start_x, start_y, end_x, end_y):
    dq = deque()
    dq.append((start_x, start_y))
    while dq:
        x, y = dq.popleft()
        if x == end_x and y == end_y:
            return graph[x][y]
        for k in range(8):
            nx = x + dx[k]
            ny = y + dy[k]
            
            if is_valid_coord(nx, ny) and graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                dq.append((nx, ny))


N = int(input().rstrip())
for _ in range(N):
    I = int(input().rstrip())
    graph = [ [0] * I for _ in range(I) ]
    start_x, start_y = map(int, input().rstrip().split())
    end_x, end_y = map(int, input().rstrip().split())

    print(bfs(start_x, start_y, end_x, end_y))
