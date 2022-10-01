import sys

input = sys.stdin.readline

N = int(input())

A = [ int(input()) for _ in range(N) ]

A.sort()

answer = -1

for i in range(N-1, 1, -1):
    if A[i] < A[i-1] + A[i-2]:
        answer = A[i] + A[i-1] + A[i-2]
        break

print(answer)

