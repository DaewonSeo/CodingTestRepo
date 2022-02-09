import sys
sys.stdin=open('data/get_k_numbers.txt', 'r')

C = int(input())

for c in range(C):
    n, s, e, k = map(int, input().split())
    nums = list(map(int, input().split()))[s-1:e]
    nums.sort()
    print("#{} {}".format(c+1, nums[k-1]))

