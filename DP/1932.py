# BOJ 1932번 정수 삼각형 문제
import sys

input = sys.stdin.readline

N = int(input())
T = []
for i in range(N):
    T.append(list(map(int, input().split())))


for i in range(1, N):
    for j in range(i+1):
        if j == 0:
            T[i][j] = T[i][j] + T[i-1][j]
        elif i == j:
            T[i][j] = T[i][j] + T[i-1][j-1]
        else:
            T[i][j] = max(T[i-1][j], T[i-1][j-1]) + T[i][j]

print(max(T[N-1]))
