import sys

input=sys.stdin.readline

n = int(input())

q = [0] * 1000000
head, tail = int(len(q) / 2), int(len(q) / 2)

for _ in range(n):
    command = input().rstrip().split()
    if command[0] == 'push_front':
        if (tail-head):
            q[head-1] = command[1]
            head -= 1
        else:
            q[head] = command[1]
            tail += 1
    
    elif command[0] == 'push_back':
        q[tail] = command[1]
        tail += 1

    elif command[0] == 'pop_front':
        if (tail-head):
            print(q[head])
            head += 1
        else: print(-1)

    elif command[0] == 'pop_back':
        if (tail-head):
            print(q[tail-1])
            tail -= 1
        else: print(-1)

    elif command[0] == 'size':
        print(tail - head)

    elif command[0] == 'empty':
        if (tail - head): print(0)
        else: print(1)

    elif command[0] == 'front':
        if (tail - head): print(q[head])
        else: print(-1)

    elif command[0] == 'back':
        if (tail - head): print(q[tail-1])
        else: print(-1)