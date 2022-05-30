# boj 2309 일곱난장이
from itertools import combinations
import sys

input = sys.stdin.readline


total_hobits = [ int(input()) for _ in range(9) ]

for heights in combinations(total_hobits, 7):
    if sum(heights) == 100:
        real_hobits = sorted(heights)

for hobit in real_hobits:
    print(hobit)