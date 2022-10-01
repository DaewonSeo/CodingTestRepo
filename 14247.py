import sys

input = sys.stdin.readline

n = int(input())

H = list(map(int, input().split()))
A = list(map(int, input().split()))
I = list(range(n))
I = sorted(I, key=lambda i: A[i])

answer = 0

for i in range(n):
    INDEX = I[i]
    answer += H[INDEX] + i * A[INDEX]

print(answer) 



# print(sum(H) - sum(A))