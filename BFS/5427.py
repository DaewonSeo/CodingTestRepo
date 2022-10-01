# 백준 5427번 불
from collections import deque
import sys

input = sys.stdin.readline

dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

# def coord

def bfs(start_x, start_y):
    dq = deque()
    dq.append((start_x, start_y))

    while dq:
        x, y = dq.popleft()
        for i in range(4):
            x = x + dx[i]
            y = y + dy[i]





T = int(input().rstrip())

for _ in range(T):
    w, h = map(int, input().rstrip().split())
    graph = [ list(input().rstrip()) for _ in range(h) ]
    

    print(graph)