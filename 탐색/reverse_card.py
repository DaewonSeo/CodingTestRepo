import sys

sys.stdin=open('../data/reverse_card.txt', 'r')

# 1~20까지 배열
cards = list(range(1, 21))

for i in range(10):
    start, end = map(int, input().split())
    # 구간 사이즈 구하기, 길이는 +1 필요
    size = end - start + 1
    for j in range(size // 2):
        # 파이썬 스왑
        cards[start-1+j], cards[end-1-j] = cards[end-1-j], cards[start-1+j]

        # 기존 풀이
        # tmp = cards[end-1-j]
        # cards[end-1-j] = cards[start-1+j]
        # cards[start-1+j] = tmp

for i in cards:
    print(i, end=' ')