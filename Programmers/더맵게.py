def solution(scoville, K):
    import heapq as hq

    answer = 0
    s = []
    for sco in scoville:
        hq.heappush(s, sco)

    while s[0] < K:
        mixed_scoville_score = hq.heappop(s) + (hq.heappop(s) * 2)
        hq.heappush(s, mixed_scoville_score)
        answer += 1
         
    
    return answer


print(solution([1, 2, 3, 9, 10, 12], 7))