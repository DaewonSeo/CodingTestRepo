# 이코테 DFS 얼음 얼려먹기
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

graph = [ list(map(int, input().rstrip())) for _ in range(N)]

def dfs(x, y):
    if x <= -1 or x >= N or y <= -1 or y <= M:
        return False

    if graph[x][y] == 0:
        graph[x][y] = 1

        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False

cnt = 0
for i in range(N):
    for j in range(M):
        if dfs(i, j) == True:
            cnt += 1

print(cnt)