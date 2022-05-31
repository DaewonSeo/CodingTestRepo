# 백준 1302 베스트셀러

import sys

input = sys.stdin.readline

N = int(input().rstrip())

solded_book = dict()

for _ in range(N):
    book_name = input().rstrip()
    if book_name in solded_book:
        solded_book[book_name] += 1
    else:
        solded_book[book_name] = 1


solded_book = sorted(solded_book.items(), key= lambda x: (-x[1], x[0]))
print(solded_book[0][0])