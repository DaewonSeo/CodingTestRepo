# boj 11286 절댓값힙
# 절댓값으로 배열 정렬을 하는 건데 

import heapq
import sys

#튜플로 푸는 방식
input = sys.stdin.readline
N = int(input().rstrip())
hq = []

for _ in range(N):
    k = int(input().rstrip())
    if k == 0:
        if len(hq) == 0:
            print(0)
        else:
            print(heapq.heappop(hq)[1])

    else:
        heapq.heappush(hq, (abs(k), k))





