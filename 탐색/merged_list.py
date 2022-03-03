import sys

sys.stdin=open('../data/merged_list.txt', 'r')

n = int(input())
n_list = list(map(int, input().split()))

k = int(input())
k_list = list(map(int, input().split()))

# O(nlogn) 풀이
# merged_list = n_list + k_list
# merged_list.sort()

# O(n) 풀이
p1, p2 = 0, 0

m = []

while p1 < n and p2 < k:
    if n_list[p1] <= k_list[p2]:
        m.append(n_list[p1])
        p1 += 1
    else:
        m.append(k_list[p2])
        p2 += 1

if p1 < n:
    m = m + n_list[p1:]

if p2 < k:
    m = m + k_list[p2:]


for i in m:
    print(i, end=' ')