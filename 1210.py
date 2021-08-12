# 다리가 있을 때 사다리 타기해주는 모듈
def letsgo(arr, r, c):
    start = c  # 출발한 인덱스 저장
    while r < 99:

        r = r + dr[0]  # 아래로 이동먼저 (이렇게 해야 왼,오 이동 후에 다시 반대로 도는 현상이 없다.)

        if c - 1 > -1 and arr[r][c - 1] == 1:  # 가장 왼쪽 다리가 아니고, 왼쪽에 길이 있으면
            while arr[r][c - 1] == 1:  # 왼쪽 끝까지 이동
                c += dc[2]
                if c == 0:  # 가장 앞지점으로 오면 break(이 문장이 없으면 오른쪽끝 사다리로 가서 while문 돌아버림)
                    break

        elif c + 1 < 100 and arr[r][c + 1] == 1:  # 가장 오른쪽 다리가 아니고, 오른쪽에 길이 있으면
            while arr[r][c + 1] == 1:  # 오른쪽 끝까지 이동
                c += dc[1]
                if c == 99:
                    break  # 가장 끝지점으로 왔을 때 break

    # 마지막 지점이 2인지 아닌지 확인
    if arr[r][c] == 1:
        return 0
    if arr[r][c] == 2:
        return start


# main
for _ in range(10):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    dr = [1, 0, 0]  # 아래, 오, 왼
    dc = [0, 1, -1]

    r = 0
    c = 0
    # print(arr)
    for start_idx in range(100):
        r = 0
        c = start_idx
        if arr[r][c] == 1:  # 다리가 있는 경우
            arrive = letsgo(arr, r, c)  # 사다리 타기
            if arrive:
                print('#{} {}'.format(tc, arrive))
                break
