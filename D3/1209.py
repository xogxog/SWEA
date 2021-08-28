# [S/W 문제해결 기본] 2일차 - Sum
# 다음 100X100의 2차원 배열이 주어질 때, 각 행의 합, 각 열의 합, 각 대각선의 합 중 최댓값을 구하는 프로그램을 작성하여라.

# 다음과 같은 5X5 배열에서 최댓값은 29이다.

# 가로 max값 뽑기
def Max_row(ls):
    max_row = 0  # 가장 큰값 받을 변수
    for i in range(len(ls)):
        curr_row_total = 0
        for j in range(len(ls[i])):
            curr_row_total += ls[i][j]  # row 고정, col +1 하면서 총값 구하기
        if max_row < curr_row_total:  # 큰값 넣기
            max_row = curr_row_total

    return Max_col(max_row, ls)  # 가로 가장 큰값과 리스트를 세로 max값 뽑는 함수로 넘겨줌
    # return max_row


# 세로 max값 뽑기
def Max_col(is_max, ls):
    max_col = 0  # 가장 큰값 받을 변수
    for i in range(len(ls)):
        curr_row_total = 0
        for j in range(len(ls[i])):
            curr_row_total += ls[j][i]  # col고정, row +1 하면서 총값 구하기
        if max_col < curr_row_total:
            max_col = curr_row_total
    # 받아온 max값(is_max)과 새로 뽑은 max값 비교해서 큰값을 대각선 뽑는 함수로 넘겨줌.
    if is_max > max_col:
        return Max_diag_1(is_max, ls)
    else:
        return Max_diag_1(max_col, ls)
    # return max_col


# 대각선 위->아래 max값 뽑기
def Max_diag_1(is_max, ls):
    max_diag_1 = 0
    curr_row_total = 0
    row = 0
    col = 0
    while col < len(ls):
        curr_row_total += ls[row][col]
        row += 1  # row 증가
        col += 1  # col 증가
        if max_diag_1 < curr_row_total:  # 최대값 넣어주기
            max_diag_1 = curr_row_total

    # 받아온 max값(is_max)과 새로 뽑은 max값 비교해서 큰값을 대각선 뽑는 함수로 넘겨줌.
    if is_max > max_diag_1:
        return Max_diag_2(is_max, ls)
    else:
        return Max_diag_2(max_diag_1, ls)
    # return max_diag_1


# 대각선 아래->위 max값 뽑기
def Max_diag_2(is_max, ls):
    max_diag_2 = 0
    curr_row_total = 0
    row = len(ls) - 1  # 아래->위 방향으로 뽑을 것이므로 row를 최대로 줌
    col = 0  # 왼 ->오 방향으로 갈것이므로 0
    while col < len(ls):
        curr_row_total += ls[row][col]
        row -= 1  # 위로
        col += 1  # 오른쪽으로
        if max_diag_2 < curr_row_total:
            max_diag_2 = curr_row_total
    # 최종적으로 제일 큰값 return
    if is_max > max_diag_2:
        return is_max
    else:
        return max_diag_2


for T in range(1, 11):
    tc = int(input())
    num_ls = [[int(row) for row in input().split()] for col in range(100)]

    print('#{} {}'.format(T, Max_row(num_ls)))
