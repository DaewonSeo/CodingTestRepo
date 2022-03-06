# 스택을 사용한 괄호 쌍 찾기 문제

import sys

input=sys.stdin.readline

while True:
    cnt = 0
    stack = []
    t = input().rstrip()
    if t == '.':
        break
    for i in t:
        if i == '(' or i == '[':
            stack.append(i)
        elif i == ')':
            if len(stack) == 0:
                cnt += 1
            else:
                if stack.pop() == '(':
                    pass
                else:
                    cnt += 1
        elif i == ']':
            if len(stack) == 0:
                cnt += 1
            else:
                if stack.pop() == '[':
                    pass
                else:
                    cnt += 1


    if len(stack) > 0 or cnt > 0:
        print('no')
    
    else:
        print('yes')
