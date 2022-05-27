# boj 10828.py

import sys
input = sys.stdin.readline

s = []
n = int(input())
for _ in range(n):
    command = input().split()
    if command[0] == 'push':
        s.append(command[1])
    elif command[0] == 'pop':
        if len(s) == 0:
            print(-1)
        else:
            print(s.pop())
    elif command[0] == 'size':
        print(len(s))

    elif command[0] == 'empty':
        if len(s) == 0:
            print(1)
        else:
            print(0)

    else:
        if len(s) == 0:
            print(-1)
        else:
            print(s[-1])
