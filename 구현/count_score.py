import sys

sys.stdin=open('../data/count_score.txt', 'r')

n = int(input())

s = list(map(int, input().split()))

bonus = 0
score = 0
for i in range(n):
    if s[i] == 1:
        bonus+=1
        score+=bonus
    else:
        bonus = 0

print(score)