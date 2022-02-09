import sys

sys.stdin=open('../data/dice_game.txt', 'r')

n = int(input())

res = 0
for i in range(n):
    tmp = input().split()
    tmp.sort()

    a, b, c = list(map(int, tmp))

    if a == b and b == c:
        price = 10000 + (a * 1000)
    elif a == b or a == c:
        price = 1000 + (a * 100)
    
    elif b == c:
        price = 1000 + (b * 100)

    else:
        price = c * 100

    if price > res:
        res = price

print(res)

