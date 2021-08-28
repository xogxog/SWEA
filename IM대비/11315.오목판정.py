# 11315. 오목 판정
T = int(input())

def wei_hei(arr) :

    for i in range(N):
        cnt_1 = 0
        cnt_2 = 0
        for j in range(N) :
            if arr[i][j] =='o':
                cnt_1 += 1
                if cnt_1 >= 5 :
                    return 'YES'
            else :
                cnt_1 = 0
            if arr[j][i] == 'o':
                cnt_2 += 1
                if cnt_2 >= 5:
                    return 'YES'
            else :
                cnt_2 = 0
    return 'NO'

def cross(arr) :
    dr = [1] # 오른아래
    dc = [1]
    # 오른아래

    for k in range(N):
        r_3 = k
        for l in range(N):
            c_3 = l
            cnt_3 = 0
            cnt_4 = 0
            if arr[r_3][c_3] == 'o': cnt_3 += 1
            if arr[c_3][r_3] == 'o' : cnt_4 += 1
            while 0<= r_3 + dr[0] < N and 0<= c_3 + dc[0] <N :
                r_3 = r_3 + dr[0]
                c_3 = c_3 + dc[0]
                if arr[r_3][c_3] == 'o':
                    cnt_3 += 1
                    if cnt_3 >=5 :
                        return 'YES'
                else :
                    cnt_3 = 0
                if arr[c_3][r_3] =='o' :
                    cnt_4 +=1
                    if cnt_4 >= 5:
                        return 'YES'
                else:
                    cnt_4 = 0

    return 'NO'

for tc in range(1,T+1) :
    N = int(input())

    omok = [input() for _ in range(N)]

    result_1 = wei_hei(omok)
    rev_omok = list(reversed(omok))
    result_2 = cross(omok)
    result_3 = cross(rev_omok)

    if result_1 == 'YES' or result_2 == 'YES' or result_3 == 'YES' :
        print('#{} {}'.format(tc,'YES'))
    else :
        print('#{} {}'.format(tc, 'NO'))