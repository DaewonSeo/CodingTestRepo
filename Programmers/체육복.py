def solutions(n, lost, reserve):
    set_reserve = set(reserve) - set(lost)
    set_lost = set(lost) - set(reserve)
    # d = dict()
    print(set_reserve, set_lost)

    for i in set_reserve:
        print(i)
        if (i-1) in set_lost:
            set_lost.remove(i-1)
        elif (i+1) in set_lost:
            set_lost.remove(i+1)

    return n - len(set_lost)
   

n = 5
lost = [2, 4]
reserve = [1, 3, 5]

print(solutions(5, lost, reserve))

    # d = dict()

    # duplicated = list(set(lost) & set(reserve))
    # for i in range(0, n+2):
    #     if i in duplicated:
    #         d[i] = 1
    #     elif i in lost:
    #         d[i] = 0
    #     elif i in reserve:
    #         d[i] = 2
    #     else:
    #         d[i] = 1

    # for l in lost:
    #     if d[l] == 1:
    #         pass
    #     else:
    #         if d[l-1] == 2:
    #             d[l] += 1
    #             d[l-1] -= 1
    #         elif d[l+1] == 2:
    #             d[l]+= 1
    #             d[l+1] -= 1
                
    # answer = 0
    # for i in range(1, n+1):
    #     if d[i] > 0:
    #         answer += 1        

    # return answer