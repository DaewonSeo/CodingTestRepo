import sys

sys.stdin=open('../data/palindrome.txt', 'r')

n = int(input())

# 문자열 슬라이싱 활용 방법
for i in range(n):
    word = input().upper()
    if word == word[::-1]:
        print('#{0} {1}'.format(i+1, "YES"))
    else:
        print('#{0} {1}'.format(i+1, "NO"))


# 문자열 순회 방법
# for i in range(n):
#     word = input().upper()
#     size = len(word)
#     for j in range(size//2):
#         if word[j] != word[-j-1]:
#             print('#{0} {1}'.format(i+1, "NO"))
#             break
#     else:
#         print('#{0} {1}'.format(i+1, "YES"))