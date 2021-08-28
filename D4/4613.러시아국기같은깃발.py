"""
2
4 5
WRWRW
BWRWB
WRWRW
RWBWR
"""

T = int(input())

for tc in range(1,T+1):
    N,M = map(int,input().split()) # N : 행, M : 열
    flag = list(input() for _ in range(N))
    min_cnt = 1000000000
    #색칠할 경계 정해주기
    for i in range(1,N-1) :

        for j in range(i+1, N) :
            cnt = 0
            # boundary.append([i,j])

            # white 갯수
            for k in range(0, i):
                for n in range(M) :
                    if flag[k][n] !='W':
                        cnt += 1
                        # print(f'화이트 : {flag[k][n]}')
                if cnt > min_cnt :
                    break
            # blue 갯수
            for l in range(i,j) :
                for o in range(M) :
                    if flag[l][o] != 'B':
                        cnt +=1
                        # print(f' 블루 : {flag[l][o]}')
                if cnt > min_cnt :
                    break
            # red 갯수
            for m in range(j,N) :
                for p in range(M) :
                    if flag[m][p] != 'R':
                        cnt +=1
            #             print(f' 레드 : {flag[m][p]}')
            # print(f'--------------------')
                if cnt > min_cnt :
                    break
            if min_cnt > cnt :
                min_cnt = cnt

    print('#{} {}'.format(tc,min_cnt))












