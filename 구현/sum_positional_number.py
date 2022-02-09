import sys

sys.stdin=open('../data/sum_positional_number.txt', 'r')

m = int(input())



nums = list(map(int, input().split()))

# cnt = [0] * m

# 내 풀이 : int를 str로 변환하여 for문을 도는 방식
# def digit_sum(x):
#     tmp = 0
#     for i in x:
#         tmp += int(i)
#     return tmp

# max = max(cnt)

# for i, v in enumerate(cnt):
#     if v == max:
#         print(nums[i])


# 강의 풀이 : %(나머지)식과 //(몫)식을 이용해서 각 자릿수 구분하는 방식
def digit_sum(x):
    sum = 0
    while x > 0:
        sum+=x%10
        x=x//10

    return sum

max = -10000000
for i in nums:
    tmp = digit_sum(i)
    if tmp > max:
        tmp = max
        res = i

print(res)

