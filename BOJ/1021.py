from collections import deque
import sys

input=sys.stdin.readline

n, k = map(int, input().rstrip().split())


q = deque(list(range(1, n+1)))
cnt = 0

nums = list(map(int, input().rstrip().split()))

for i in nums:
    idx = q.index(i)
    gap = -1 if idx <= len(q) // 2 else 1
    while q[0] != i:
        q.rotate(gap)
        cnt += 1
    q.popleft()

print(cnt)



