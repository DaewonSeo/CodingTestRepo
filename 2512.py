import sys

input=sys.stdin.readline

N = int(input())
budgets = list(map(int, input().split()))
total = int(input())

def check_range(bound):
    needed_budget = 0
    for b in budgets:
        needed_budget += min(b, bound)

    return needed_budget

low = 0
high = max(budgets)
good_upper_bound = -1

while low <= high:
    mid = (low + high) // 2

    if check_range(mid) <= total:
        low = mid + 1
        good_upper_bound = mid

    else:
        high = mid - 1

answer = -1
for b in budgets:
    given = min(b, good_upper_bound)
    answer = max(answer, given)

print(answer)

