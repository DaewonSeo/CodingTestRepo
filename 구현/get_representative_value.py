import sys

sys.stdin=open('data/get_representative_value.txt', 'r')

n = int(input())
nums = list(map(int, input().split()))

# 파이썬의 round 함수는 round_half_even 방식으로 정확하게 4.5000으로 떨어질 경우 가까운 짝수 값으로 매칭되서 값이 down 되는 경우가 있음.
# 대처법으로 해당 수에 0.5를 더해준 뒤 int로 형 변환을 해주면 된다.

avg = int((sum(nums) / n) + 0.5)


# 내 풀이
# sub = [ abs(i - avg) for i in nums]

# m = list(set(sub))
# m.sort()
# m = m[0] # 최소 차이

# s = 0
# index = 0
# for i in range(n):
#     if sub[i] == m and nums[i] > s: 
#         s = nums[i]
#         index = i 
        
# print(avg, index+1)

# 강의 풀이

min = float('inf')
for i, v in enumerate(nums):
    tmp = abs(v - avg)
    if tmp < min:
        min = tmp
        score = v
        idx = i + 1
    
    elif tmp == min:
        if v > score:
            score = v
            idx = i + 1

print(avg, idx) 
