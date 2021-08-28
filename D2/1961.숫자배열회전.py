import copy

T = int(input())


def t_swap(list):
    #전치
    for i in range(0, N):
        for j in range(0, N):
            if i<j :
                list[i][j],list[j][i] = list[j][i],list[i][j]

    # 거꾸로 swap
    for k in range(0,N):
        for l in range(0,N//2) :
            list[k][l],list[k][N-1-l] = list[k][N-1-l],list[k][l]
    return list

for tc in range(0, T):
    N = int(input())
    N_list = [list(map(int, input().split())) for _ in range(N)]

    # print(N_list)

    t_N_list = t_swap(N_list)

    t_N_list_2 = t_swap(copy.deepcopy(t_N_list))

    t_N_list_3 = t_swap(copy.deepcopy(t_N_list_2))


    print('#{}'.format(tc+1))
    for i in range(0,N) :
        print('{} {} {}'.format(''.join(map(str,t_N_list[i])),''.join(map(str,t_N_list_2[i])) ,''.join(map(str,t_N_list_3[i]))))
