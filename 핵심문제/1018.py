# 백준 1018번 문제 체스판 다시 칠하기

import sys

input = sys.stdin.readline


N, M = map(int, input().split())
board = [ list(input().rstrip()) for _ in range(N)]

answer = 64

def fill(y, x, bw):
    global answer
    cnt = 0
    for i in range(8):
        for j in range(8):
            if (i+j) % 2:
                if board[y+i][x+j] == bw:
                    cnt += 1
            
            else:
                if board[y+i][x+j] != bw:
                    cnt += 1

    answer = min(answer, cnt)


for i in range(N - 7):
    for j in range(M - 7):
        fill(i, j, 'B')
        fill(i, j, 'W')

print(answer)