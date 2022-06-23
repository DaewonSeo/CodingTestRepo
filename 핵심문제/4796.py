# 백준 4796번 캠핑 문제

import sys

input = sys.stdin.readline
i = 1
while True:
    L, P, V = map(int, input().rstrip().split())
    if (L+P+V) == 0:
        break

    print(f'Case {i}: {V//P * L + min(V%P, L)}')
    i += 1

    #좀 더 긴 풀이
    # else:
        # vac = (V//P) * L
        # rest = (V%P)
        # if rest >= L:
        #     vac += L
        # else:
        #     vac += rest
        # print(f'Case {i}: {vac}')


