import sys

input = sys.stdin.readline

N, T = map(int, input().split())

TArr = list(map(int, input().split()))

start, end = 0, max(TArr)

while start <= end:
    mid = (start + end) // 2
    cnt = 0
    Arr = TArr.copy()
    for i in range(N-1):
        if Arr[i] < Arr[i+1] and Arr[i+1] - Arr[i] > mid:
            distance = Arr[i+1] - Arr[i] - mid
            Arr[i+1] -= distance
            cnt += distance
        # print(f'최솟값 : {mid}, 인덱스 i : {i}, {Arr}, 횟수 : {cnt}')

    for j in range(N-1, 0, -1):
        if Arr[j] < Arr[j-1] and Arr[j-1] - Arr[j] > mid:
            distance = Arr[j-1] - Arr[j] - mid
            Arr[j-1] -= distance
            cnt += distance
        # print(f'최솟값 : {mid}, 인덱스 j : {j}, {Arr}, 횟수: {cnt}')
    # print(f'횟수 : {cnt}')
    if cnt <= T:
        answer = Arr
        end = mid - 1
    else:
        start = mid + 1

print(' '.join(map(str, answer)))
            

            

