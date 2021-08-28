
T = int(input())


for tc in range(T) :
    N = int(input())

    arr = [[0]*N for _ in range(N)] # 2차원 배열 생성

    #우 하 좌 상
    dr = [0, 1, 0, -1] # 행
    dc = [1, 0, -1, 0] # 열

    arr = [[0]*N for _ in range(N)]
    cnt = 1
    i , j = 0 , -1  #출발지점 지정

    k=0 # 방향전환

    while cnt<=N*N:
        ni,nj = i+dr[k] , j+dc[k] # 이동
        if 0<= ni < N and 0<= nj < N and arr[ni][nj] == 0 :
            arr[ni][nj] = cnt
            cnt += 1
            i , j = ni , nj
        else :
            #if k == 4 : k ==0 으로 해도 된다.
            k = (k+1) % 4 #어떤 값을 삥글삥글 돌게하고싶을때 사용하자!!나머지 연산!!


    for i in range(N):
        for j in range(N) :
            print(arr[i][j],end=" ")
        print()