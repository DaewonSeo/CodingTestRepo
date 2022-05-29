#boj 2164번 카드 2

from collections import deque
import sys

input = sys.stdin.readline


N = int(input().rstrip())
dq = deque(range(1, N+1))


while len(dq) > 1:
    dq.popleft()
    dq.rotate(-1)

print(dq.pop())