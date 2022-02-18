# 프로그래머스 / 해시 / 위장
clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]

def solution(clothes):
    d = dict()
    for name, category in clothes:
        if category in d:
            d[category] += 1
        else:
            d[category] = 1
    
    
    answer = 1
    for k, v in d.items():
        answer *= (v+1)
    
    return answer - 1

print(solution(clothes))