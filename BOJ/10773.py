import sys

input=sys.stdin.readline

n = int(input())

stack = []
for _ in range(n):
    k = int(input())
    if k: stack.append(k) 
    else: stack.pop()

print(sum(stack))