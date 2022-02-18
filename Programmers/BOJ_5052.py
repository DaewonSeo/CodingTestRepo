import sys
input = sys.stdin.readline

n = int(input().rstrip())
answer = []
for _ in range(n):
    k = int(input().rstrip())
    phone_book = []

    for _ in range(k):
        phone = input().rstrip()
        phone_book.append(phone)

    phone_book.sort()
    for i in range(len(phone_book) - 1):
        if phone_book[i+1].startswith(phone_book[i]):
            answer.append('NO')
            break
    else:
        answer.append('YES')
    
for i in answer:
    print(i)