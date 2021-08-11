T=int(input())

for tc in range(T) :
    N,M = map(int, input().split())
    N_ls = [int(i) for i in input().split()]

    #print(N,M,N_ls)

    max_tot = 0
    min_tot = 0
    for n in range(len(N_ls)-M+1) :
        curr_tot =0
        for m in N_ls[n:n+M] :
            curr_tot += m


        if min_tot == 0 : #최소합 초기화(조건에서 주어지져서 필요없는 문장일 수 있다)
            min_tot = curr_tot

        elif min_tot > curr_tot:
            min_tot = curr_tot

        if max_tot < curr_tot :
            max_tot = curr_tot

    print('#{} {}'.format(tc+1,max_tot-min_tot))