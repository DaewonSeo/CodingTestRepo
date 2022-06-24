#백준 1389번 케빈 베이컨의 6단계 법칙

import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

graph = [ [] for _ in range(N)]

for _ in range(M):
    a, b = map(lambda x: x-1, map(int, input().rstrip().split()))
    graph[a].append(b)
    graph[b].append(a)



def bfs(start, end):
    chk = [False] * N
    chk[start] = True
    dq = deque()
    dq.append((start, 0))
    while dq:
        now, d = dq.popleft()
        if now == end:
            return d
        nd = d + 1
        for nxt in graph[now]:
            if not chk[nxt]:
                chk[nxt] = True
                dq.append((nxt, nd))
    return d



def get_kevin(start):
    tot = 0
    for i in range(N):
        if i != start:
            tot += bfs(start, i)
    return tot

ans = (-1, 987654321)

kevins = []

for i in range(N):
    kevins.append(get_kevin(i))


for i, v in enumerate(kevins):
    if ans[1] > v:
        ans = (i, v)

print(ans[0] + 1)