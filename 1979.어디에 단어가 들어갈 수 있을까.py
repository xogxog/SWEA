T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())  # N * N 크기의 퍼즐, 글자 수
    puzzle = [list(map(int, input().split())) for _ in range(N)]
    #print(* puzzle)

    # 글자수만큼 들어갈 수 있는 갯수
    over_K_blank = 0

    for r_1 in range(N):
        cnt_r = 0
        for c_1 in range(N):
            # 가로
            if puzzle[r_1][c_1] == 0:
                if cnt_r == K:
                    over_K_blank += 1
                cnt_r = 0
                continue
            elif puzzle[r_1][c_1] == 1:
                cnt_r += 1

                if c_1 == N-1 : #마지막 자리면
                    if cnt_r == K:
                        over_K_blank += 1

    for r_2 in range(N):
        cnt_c = 0
        for c_2 in range(N):
            # 세로
            if puzzle[c_2][r_2] == 0:
                if cnt_c == K:
                    over_K_blank += 1
                cnt_c = 0
                continue
            elif puzzle[c_2][r_2] == 1:
                cnt_c += 1
                if c_2 == N-1 : #마지막 자리면
                    if cnt_c == K:
                        over_K_blank += 1
    print('#{} {}'.format(tc,over_K_blank))
