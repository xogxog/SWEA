# 7 3 6 4 2 9 5 8 1
# 5 8 9 1 6 7 3 2 4
# 2 1 4 5 8 3 6 9 7
# 8 4 7 9 3 6 1 5 2
# 1 5 3 8 4 2 9 7 6
# 9 6 2 7 5 1 8 4 3
# 4 2 1 3 9 8 7 6 5
# 3 9 5 6 7 4 2 1 8
# 6 7 8 2 1 5 4 3 9
import copy


def r_c_overlap(sudoku):
    #가로
    for ii in range(9):
        cnt = [0] * 10
        for jj in range(9):
            if cnt[sudoku[ii][jj]] == 0:
                # if cnt[sudoku[ii][jj]] != 0:  # 중복되는 숫자가 있으면 0
                #     return 0
                cnt[sudoku[ii][jj]] += 1
                #print(cnt)
            else :
                return 0

    #세로
    for ii in range(9):
        t_cnt = [0] * 10
        for jj in range(9):
            if t_cnt[sudoku[jj][ii]] == 0:
                t_cnt[sudoku[jj][ii]] += 1
                #print(t_cnt)
            else :
                return 0




    #return 1

    #사각형
    for k in range(0, 9, 3):
        for m in range(0,9,3) :
            square = [sudoku[k:k+3] for sudoku in sudoku[m:m+3]]
            #print(square)
            squ_cnt = [0] * 10
            for o in range(0, len(square)) :
                #print(o)
                for p in range(0, len(square[o])) :
                    print(square[o][p])
                    if squ_cnt[square[o][p]] == 0 :
                        squ_cnt[square[o][p]] += 1
                    else :
                        return 0

    return 1


T = int(input())

for tc in range(1, T + 1):
    sudoku = [list(map(int, input().split())) for _ in range(9)]
    # print(sudoku)


    # 가로세로 중복 값 있는지 확인
    result = r_c_overlap(sudoku)

    print('#{} {}'.format(tc,result))


