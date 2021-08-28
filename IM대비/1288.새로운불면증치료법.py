T = int(input())

for tc in range(1,1+T) :
    N = int(input())
    _num = 1
    cnt =[]
    flag = 0
    while True :
        _num_multi = str(_num * N)
        for i in range(len(_num_multi)) :
            if _num_multi[i] not in cnt :
                cnt.append(_num_multi[i])
            if len(cnt) >= 10 :
                flag = 1
                break
        if flag :
            break
        _num += 1

    print('#{} {}'.format(tc, _num_multi))