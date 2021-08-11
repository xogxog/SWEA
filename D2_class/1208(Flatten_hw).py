
for tc in range(10) :
    lim_N = int(input())
    ls = list(map(int, input().split()))
    #print(ls)

    #정렬
    # for i in range(len(ls)-1) :
    #     for j in range(i+1,len(ls)) :
    #         if ls[i] > ls[j] :
    #             ls[i],ls[j]=ls[j],ls[i]
    #             print(ls)


    min_idx, max_idx = 0,0
    cnt =0
    while cnt<=lim_N :
        min_num, max_num = 100, 1
        for idx in range(len(ls)) :
            if min_num >ls[idx] :
                min_num = ls[idx]
                min_idx = idx
            if max_num < ls[idx] :
                max_num = ls[idx]
                max_idx = idx
        if max_num - min_num <=1 :
            print('#{} {}'.format(tc+1,max_num-min_num))
            break
        else :
            ls[min_idx] +=1
            ls[max_idx] -=1
            cnt +=1
            if cnt >= 13 :
                print(min_num, max_num)
                print(cnt)
        #print(max_num, min_num)
            if cnt > lim_N : print('#{} {}'.format(tc+1, max_num-min_num))
