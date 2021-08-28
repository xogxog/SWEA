# dfs 가 잘 안돼서 dfs로 해봤습니다. 근데..재귀에서 종료하기가 힘들었는데,
# flag를 global변수로 써서 해결..!

dr = [1, 0, 0, -1]  # 아래,오른,왼,위
dc = [0, 1, -1, 0]


def Mymaze(start):
    global flag
    stack = [start]

    while stack:  # 도착할 때 까지 돕니다.
        curr_r, curr_c = stack.pop()
        flag = 0
        maze[curr_r][curr_c] = "x"

        for i in range(4):
            nr = curr_r + dr[i]
            nc = curr_c + dc[i]
            if maze[nr][nc] == 3:
                flag = 1
                return 1
            if 0 <= nr < 16 and 0 <= nc < 16 and maze[nr][nc] == 0:
                # print(f'-------------')
                # for m in range(16):
                #     print(*maze[m])
                Mymaze([nr, nc])
                if flag == 1:
                    return 1

    return 0


for _ in range(10):
    tc = int(input())
    maze = [list(map(int, input())) for _ in range(16)]

    # print(maze)
    start = []  # 시작 지점
    for i in range(16):
        for j in range(16):
            if maze[i][j] == 2:
                start.append(i)
                start.append(j)

    result = Mymaze(start)
    print("#{} {}".format(tc, result))
