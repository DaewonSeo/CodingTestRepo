# BOj 1448 수리공 항승

import sys

input = sys.stdin.readline

N, K = map(int, input().split())

hole = list(map(int, input().split()))
hole.sort()

start = hole[0]
end = start + K + 0.5
cnt = 1

for i in hole:
    if end >= i:
        continue
    else:
        cnt += 1
        end = i + K + 0.5

print(cnt)


# places = [False] * 1001

# for i in map(int, input().split()):
#     places[i] = True

# x = 0
# cnt = 0 
# while x < 1001:
#     if places[x]:
#         cnt += 1
#         x += K
#     else:
#         x += 1

# print(cnt) 