T=10

for tc in range(T) :
    N=int(input())
    ls=list(map(int,input().split()))
    #print(ls)

    cnt=0
    for n in range(2, N-2):
        right_max=ls[n]
        if ls[n] <= 0 or ls[n] <= ls[n-2] or ls[n] <= ls[n-1] or ls[n] <= ls[n+1] or ls[n] <= ls[n+2] :
            continue
        else :
            #print(ls[n])
            for i in ls[n-2:n+3] :
                if ls[n]-i == 0:
                    pass
                elif ls[n]-i < right_max :
                    right_max = ls[n]-i
            #print(f'조망권 갯수 : {right_max}')
        cnt += right_max

    print('#{0} {1}'.format(tc+1,cnt))
