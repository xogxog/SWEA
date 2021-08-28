T = int(input())

def total(arr) :
    arr_tot = 0
    for i in range(N):
        for j in range(N):
            arr_tot += arr[i][j]
    return arr_tot

def tot_minus(arr) :
    cnt = 0
    for i in range(N):
        if i <= N//2 :
            for j in range(0,N//2-i):
                cnt += arr[i][j]
        else :
            for j in range(0,i-N//2):
                cnt+= arr[i][j]
    return cnt


for tc in range(1,T+1) :
    N = int(input())
    ground = [list(map(int,input()))for _ in range(N)]
    # print(ground)
    rev_ground =[]
    for i in range(N):
        rev_ground.append(list(reversed(ground[i])))



    # print(rev_ground)

    total_cnt = total(ground)
    minus_1 = tot_minus(ground)
    minus_2 = tot_minus(rev_ground)

    result = total_cnt - minus_1 - minus_2
    print('#{} {}'.format(tc,result))