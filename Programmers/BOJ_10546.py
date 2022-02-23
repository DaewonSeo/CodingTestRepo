import sys
input = sys.stdin.readline

n = int(input().rstrip())

p = {}

for _ in range(n):
    name = input().rstrip()
    if name in p:
        p[name] += 1
    else:
        p[name] = 1

for _ in range(n-1):
    name = input().rstrip()
    p[name] -= 1

for k, v in p.items():
    if v != 0:
        print(k)
        break


    