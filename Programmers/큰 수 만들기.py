def solution(number, k):

    answer = []
    
    for num in number:
        if not answer:
            answer.append(num)
            print('1단계', answer)
            continue
        if k > 0:
            while answer[-1] < num:
                answer.pop()
                k -= 1
                if not answer or k <= 0:
                    break
        print('전', answer)
        answer.append(num)
        print('후', answer)

    answer = answer[:-k] if k > 0 else answer
    return ''.join(answer)


number = '4177252841'
k = 4

print(solution(number, k))