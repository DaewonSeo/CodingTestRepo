def solution(numbers):
    numbers = list(map(str, numbers))
    # print(numbers)
    numbers.sort(key=lambda num: num*3, reverse=True)
    answer = str(int(''.join(numbers)))
    
    return answer
    
print(solution([3, 30, 34, 5, 9]))

