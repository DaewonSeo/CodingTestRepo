# BOJ 9012.py https://www.acmicpc.net/problem/9012

import sys
input = sys.stdin.readline

n = int(input().rstrip())

for _ in range(n):
    s = []
    ps_list = list(input().rstrip())

    for ps in ps_list:
        if ps == '(':
            s.append(ps)
        elif ps == ')':
            if len(s) == 0:
                print('NO')
                break
            else:
                s.pop()
    else:
        if len(s) == 0:
            print('YES')
        else:
            print('NO')
        

     