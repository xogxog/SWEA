T = int(input())

for tc in range(1,T+1):
    N = int(input())
    ls = [list(map(int, input().split())) for _ in range(N)]


    red_ls =[] #red 칠해진 좌표를 담을 것이다.
    blue_ls=[] #blue 칠해진 좌표를 담을 것이다.

    for i in range(len(ls)) :
        if ls[i][-1] == 1 : #빨간색 리스트로갈 친구들
            for x in range(ls[i][0],ls[i][2]+1) : # x좌표
                for y in range(ls[i][1],ls[i][3]+1) : #y좌표
                    red_ls.append([x,y])
        else :
            for x in range(ls[i][0],ls[i][2]+1) : # x좌표
                for y in range(ls[i][1],ls[i][3]+1) : #y좌표
                    blue_ls.append([x,y])
    cnt = 0
    for red in red_ls :
        for blue in blue_ls :
            if red == blue :
                cnt += 1
                break

    print('#{} {}'.format(tc,cnt))