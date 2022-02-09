import sys

sys.stdin=open('../data/get_reversed_prime.txt', 'r')

n = int(input())
nums = list(map(int, input().split()))

# 내 풀이 : str으로 변환해서 reverse 처리
# def reverse(x):
#     x = str(x)
#     x = x[::-1]
#     return int(x)

# 강의 풀이 : %와 //을 활용한 변환식
"""
9010 대입시
---- 1차 연산 ----
t = 9010 % 10 : 0
res = 0 * 10 + 0 : 0 
x = 9010 // 10 : 901

---- 2차 연산 ----
t = 901 % 10 : 1
res = 0 * 10 + t : 1
x = 901 // 10 : 90

---- 3차 연산 ----
t = 90 % 10 : 0
res = 1 * 10 + 0 : 10
x = 90 // 10 : 9

---- 4차 연산 ----
t = 9 % 10 : 9
res = 10 * 10 + 9 : 109
x = 9 // 10 : 0 => while문 종료
"""
def reverse(x):
    res = 0
    while x > 0:
        t = x % 10
        res = res * 10 + t
        x = x // 10

    return res


def isPrime(x):
    if x == 1:
        return False

    for i in range(2, x//2+1):
        if x % i == 0:
            return False
    else:
        return True

for i in nums:
    tmp = reverse(i)
    if isPrime(tmp):
        print(tmp, end=' ')