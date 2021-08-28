# N2개의 방이 N×N형태로 늘어서 있다.
#
# 위에서 i번째 줄의 왼쪽에서 j번째 방에는 1이상 N2 이하의 수 Ai,j가 적혀 있으며, 이 숫자는 모든 방에 대해 서로 다르다.
#
# 당신이 어떤 방에 있다면, 상하좌우에 있는 다른 방으로 이동할 수 있다.
#
# 물론 이동하려는 방이 존재해야 하고, 이동하려는 방에 적힌 숫자가 현재 방에 적힌 숫자보다 정확히 1 더 커야 한다.
#
# 처음 어떤 수가 적힌 방에서 있어야 가장 많은 개수의 방을 이동할 수 있는지 구하는 프로그램을 작성하라.

dr = [0, 1, 0, -1]  # 우하좌상
dc = [1, 0, -1, 0]


def move_room(arr, s):
    # visit = [[0] * N for _ in range(N)]
    q = [s]  # queue
    cnt = 1  # 몇번째 이동인지 (자기자신만 갈수있으면 1로 친다)
    while q:
        r, c = q.pop(0)  # 현재 위치 설정
        # visit[r][c] = 1
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            # print(nr,nc)
            if nr < 0 or nr >= N or nc < 0 or nc >= N:  # 이동한 좌표가 범위를 넘으면 다른곳으로 이동
                continue
            if room[r][c] + 1 == room[nr][nc] :  # 이동할 곳이 그전 방보다 1 높은경우
                q.append([nr, nc])
                cnt += 1
                # visit[nr][nc] = 1  # 방문 찍고
                # print(f'시작지점 : {arr[s[0]][s[1]]} cnt : {cnt}, 방번호 : {room[r][c]}, 움직일 곳 : {room[nr][nc]}')
                # print(*visit)

    return (arr[s[0]][s[1]], cnt)  # 방번호, 카운트한거


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    room = [list(map(int, input().split())) for _ in range(N)]

    print(*room)

    max_move = 0
    max_room = 0
    for i in range(N):
        for j in range(N):
            start = [i, j]
            result = move_room(room, start)
            if max_move < result[1]:
                max_move = result[1]
                max_room = result[0]
            elif max_move == result[1]:
                if max_room > result[0] :
                    max_room = result[0]

    print('#{} {} {}'.format(tc, max_room, max_move))
