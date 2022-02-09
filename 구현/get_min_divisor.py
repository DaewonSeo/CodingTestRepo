import sys

sys.stdin=open('../data/get_min_divisor.txt', 'r') # 'rt'모드의 t는 default 값

n, k = map(int, input().split())
print(n,k)
cnt = 0
for i in range(1, n+1):
    if n % i == 0:
        cnt += 1
    
    if cnt == k:
        print(i)
        break

else:
    print(-1)