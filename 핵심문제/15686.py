#백준 15686번 치킨배달 문제

from itertools import combinations
import sys

input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

houses = []
chickens = []

for i in range(N):
    for j, v in enumerate(map(int, input().rstrip().split())):
        if v == 1:
            houses.append((i, j))
        
        elif v == 2:
            chickens.append((i, j))

ans = 2 * N * len(houses)

def get_dist(house, chickens):
    return abs(house[0] - chickens[0]) + abs(house[1] - chickens[1])

for combi in combinations(chickens, M):
    
    total = 0
    distance = []
    for house in houses:
        for c in combi:
            distance.append(get_dist(house, c))
        total+= min(distance)
        distance = []

        # total += min(distance)

        # total += min(get_dist(house, c) for c in combi)
    
    ans = min(ans, total)

print(ans)
