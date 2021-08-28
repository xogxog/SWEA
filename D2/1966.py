#정렬해보자(버블 or count정렬 사용하기)

T= int(input())

#count 정렬
def Max_num(ls) :
    Max_n = ls[0]
    for i in range(1,len(ls)) :
        if Max_n < ls[i] :
            Max_n = ls[i]
    return Max_n

for tc in range(T) :
    N=int(input())
    unsort_ls=[ int(i) for i in input().split()]
    Max_n = Max_num(unsort_ls)

    cnt_ls=[0] * (Max_n+1)

    for idx in unsort_ls :
        cnt_ls[idx] += 1

    for idx in range(1,len(cnt_ls)) :
        cnt_ls[idx] += cnt_ls[idx-1]
    #print(cnt_ls)

    tmp = [0] * N
    for idx in range(len(unsort_ls)-1,-1,-1):
        curr_num = unsort_ls[idx]
        cnt_ls[curr_num] -= 1
        tmp[cnt_ls[curr_num]] = curr_num
        #print(tmp)

    print('#{0} {1}'.format(tc+1, ' '.join(map(str, tmp))))