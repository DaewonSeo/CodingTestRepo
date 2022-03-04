import sys
import heapq as hq

input = sys.stdin.readline

n = int(input())

a = []

for _ in range(n):
    k = int(input())

    if k == 0:
        if len(a) == 0:
            print(0)
        
        else:
            print(-hq.heappop(a))

    else:
        hq.heappush(a, -k)