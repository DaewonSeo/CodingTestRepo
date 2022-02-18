from collections import defaultdict

def solution(genres, plays):
    d = dict()
    num = []
    answer = []
    for i in range(len(genres)):
        if genres[i] in d:
            d[genres[i]].append([plays[i], i])
        else:
            d[genres[i]] = [[plays[i], i]]

    for key in d.keys():
        d[key].sort(key=lambda x: (-x[0], x[1]))
    
    for key,value in d.items():
        num_sum = 0
        for v in value:
            num_sum +=v[0]
        num.append([key,num_sum])

    num.sort(key = lambda x: -x[1])


    for genre,_ in num:
        if len(d[genre]) ==1:
            answer.append(d[genre][0][1])
        else:
            answer.append(d[genre][0][1])
            answer.append(d[genre][1][1])
    return answer

    
genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]

print(solution(genres, plays))

