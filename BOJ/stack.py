import sys

input=sys.stdin.readline

n = int(input())

s = []
for i in range(n):
    e = input().split()
    if e[0] == 'push':
        s.append(int(e[1]))

    elif e[0] == 'pop':
        if len(s):
            print(s[-1])
            s.pop()
        else:
            print(-1)

    elif e[0] == 'size':
        print(len(s))

    elif e[0] == 'top':
        if len(s):
            print(s[-1])
        else:
            print(-1)

    else:
        if len(s):
            print(0)
        else:
            print(1)
            