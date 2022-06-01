from collections import deque

# 오른족, 아래, 왼쪽, 위쪽
dy = (0, 1, 0, -1)
dx = (1, 0, -1, 0)

chk = [[False] * 100 for _ in range(100)]

N = int(input())

def is_valid_coord(y, x):
    return 0 <= y < N and 0 <= x < N


def bfs(start_y, start_x):
    dq = deque()
    dq.append((start_y, start_x))

    while dq:
        y, x = dq.popleft()
        chk[y][x] = True
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            if is_valid_coord(ny, nx) and not chk[ny][nx]:
                dq.append((ny, nx))