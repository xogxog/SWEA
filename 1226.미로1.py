def Mymaze(maze, start) :
    maze[start[0]][start[1]] = 1  # 출발지점 1로 줘야 밑에 조건식에서 잘못 들어가지 않는다.
    dr = [1, 0, 0, -1]  # 아래,오른,왼,위
    dc = [0, 1, -1, 0]

    p = 0  # 방향
    checkpoint = []
    r = start[0]  # row (maze를 돌아다닐 좌표)
    c = start[1]  # col

    while True:  # 도착할 때 까지 돕니다.

        while maze[r + 1][c] + maze[r][c + 1] + maze[r - 1][c] + maze[r][c - 1]!= 4:  # 막다른길이 아니면
            check = maze[r + 1][c] + maze[r][c + 1] + maze[r - 1][c] + maze[r][c - 1]
            if check < 3:  # 갈림길이라면
                maze[r][c] = 1  # 일단 방문 표시하고
                checkpoint.append([r, c, 3 - check])  # 갈림길 , 남은 갈림길 갯수 표시
            if maze[r + dr[p]][c + dc[p]] == 0 or maze[r + dr[p]][c + dc[p]] == 3:  # (아래,오른,왼,위)방향에 길이 있으면
                r += dr[p]
                c += dc[p]
                if maze[r][c] == 3 :
                    return 1
                maze[r][c] = 1  # 방문 표시
                p = 0

            else:
                p = (1 + p) % 4

        if maze[r + 1][c] + maze[r][c + 1] + maze[r - 1][c] + maze[r][c - 1] == 4:  # 막다른 길이라면
            for i in range(len(checkpoint) - 1, -1, -1):
                if checkpoint[i][2] > 0:  # 아직 방문하지 않은 갈림길이 있다면
                    r = checkpoint[i][0]  # checkpoint의 좌표로 가게 합니다.
                    c = checkpoint[i][1]  # checkpoint의 좌표로 가게 합니다.
                    checkpoint[i][2] -= 1  # 갈림길 갯수 -
                    break
                elif i == 0 and checkpoint[i][2] == 0:  # 가장 상위 갈림길인데 갈림길이 없으면 도착X
                    return 0




for _ in range(10) :
    tc = int(input())
    maze = [list(map(int,input())) for _ in range(16)]

    # print(maze)
    start=[] # 시작 지점
    for i in range(16):
        for j in range(16) :
            if maze[i][j] == 2 :
                start.append(i)
                start.append(j)

    result = Mymaze(maze,start)
    print("#{} {}".format(tc,result))




