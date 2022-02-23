import sys

sys.stdin=open('../data/extract_num.txt', 'r')

s = input().rstrip()

"""
tip : 굳이 문자에서 수로 자료형을 변환하지 않아도 0을 소거하는 방법이 있음
res = 0
res = res * 10 + int(i)
"""

num = ''
for i in s:
    if i.isdigit():
        num += i
        # num = num * 10 + int(i)

num = int(num)
print(num)

count = 0
for i in range(1, num+1):
    if num % i == 0:
        count += 1

print(count) 
