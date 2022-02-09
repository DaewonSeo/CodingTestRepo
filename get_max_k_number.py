import sys

sys.stdin=open('data/get_max_k_number.txt', 'r')

n, k = map(int, input().split())
nums = list(map(int, input().split()))
res = set()

for i in range(n):
    for j in range(i+1, n):
        for m in range(j+1, n):
            res.add(nums[i]+nums[j]+nums[m])

res = list(res)
res.sort(reverse=True)
print(res[k-1])


