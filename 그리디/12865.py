# 백준 12865문제 평범한 배낭

import sys

input = sys.stdin.readline

N, K = map(int, input().split())


cargo = [ list(map(int, input().split())) for _ in range(N) ]
    
pack = [ (c[1]/c[0], c[0], c[1]) for c in cargo ]
# pack.sort(key=lambda x: (x[0], -x[1]))


V = 0
for p in pack:
    if K - p[1] >= 0:
        K -= p[1]
        V += p[2]
    else:
        left = K / p[1]
        V += left * p[2]

print(int(V))

