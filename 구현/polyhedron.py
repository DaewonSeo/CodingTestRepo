import sys
sys.stdin=open('../data/polyhedron.txt', 'r')

n, k = map(int, input().split())

cnt = [0] * (n+k+1)

for i in range(1, n+1):

    for j in range(1, k+1):
        cnt[i+j] +=1
        
max = max(cnt)
for i, v in enumerate(cnt):
    if v == max:
        print(i, end=' ')

