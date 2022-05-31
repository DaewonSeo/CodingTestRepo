# BOJ 11047 동전 0

import sys

input = sys.stdin.readline

N, K = map(int, (input().split()))

coins = [ int(input().strip()) for _ in range(N) ][::-1]
cnt = 0

for coin in coins:
    cnt += K // coin
    K %= coin
    # if coin <= K:
    #     if (K % coin) == 0:
    #         cnt += (K // coin)
    #         break
    #     else:
    #         cnt += (K // coin)
    #         K = (K % coin)

print(cnt)


    
