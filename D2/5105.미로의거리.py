# 5105. [파이썬 S/W 문제해결 기본] 6일차 - 미로의 거리

T = int(input())

def start_end_point(maze) :
    start = [0, 0]  # 출발지점
    end = [0, 0]    # 끝지점
    s_flag = 0
    e_flag = 0
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2 :
                start[0] = i
                start[1] = j
                s_flag =1
            if maze[i][j] == 3 :
                end[0] = i
                end[1] = j
                e_flag = 1
            if s_flag and e_flag :
                return start, end


def find_road(arr,s) : # 미로, 출발지점 받아옴
    dr = [0,-1,0,1] # 좌상우하
    dc = [-1,0,1,0]
    start = s
    q = [start]
    arr[start[0]][start[1]] = 1 #출발지점 1로 표시
    while q :
        curr_r, curr_c = q.pop(0)
        for i in range(4):
            nr = curr_r + dr[i]
            nc = curr_c + dc[i]

            if 0<=nr<N and 0<=nc<N :         # 범위안에있고,

                if arr[nr][nc] == 'X':          # 움직이려는 곳에 도착지점이 있으면
                    return arr[curr_r][curr_c] - 1

                elif arr[nr][nc] == 0 :         # 방문안했으면
                    q.append([nr,nc])                           #queue에 넣어주고
                    arr[nr][nc] = arr[curr_r][curr_c] + 1       # 그전칸에서 한칸 멀어진 것 표시(방문표시)
                    # print(f'========미로============')
                    # for m in range(N):
                    #     print(*arr[m])
                    # print(f'========미로============')
    return 0




for tc in range(1,T+1) :
    N = int(input())

    maze = [list(map(int,input())) for _ in range(N)]

    start, end = start_end_point(maze)
    maze[end[0]][end[1]] = 'X'          # 끝지점 따로 표시(visited를 따로 만들지 않을거라서)

    result = find_road(maze,start)
    print('#{} {}'.format(tc,result))


