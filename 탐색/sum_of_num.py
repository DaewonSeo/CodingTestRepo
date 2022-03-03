import sys

sys.stdin=open('../data/sum_of_num.txt', 'r')

n, k = map(int, input().split())
l = list(map(int, input().split()))

lt = 0
rt = 1
res = l[0]
cnt = 0

while True:
    if res < k:
        if rt < n:
            res += l[rt]
            rt += 1
        else:
            break
    
    elif res == k:
        cnt += 1
        res -= l[lt]
        lt += 1
    else:
        res -= l[lt]
        lt += 1
    
print(cnt)

# for i in 