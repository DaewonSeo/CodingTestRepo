# 백준 2841번 외계인의 기타 연주 

import sys
import heapq

input = sys.stdin.readline

N, P = map(int, input().rstrip().split())


stk = [[] for _ in range(7)]
# stk = []
cnt = 0
for _ in range(N):
    line, p = map(int, input().rstrip().split())
    while stk[line] and stk[line][-1] > p:
        stk[line].pop()
        cnt += 1
    
    if stk[line] and stk[line][-1] == p:
        continue

    stk[line].append(p)
    cnt += 1
        
print(cnt)
