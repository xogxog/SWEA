# 도착한걸 아는 방법은 도착지점인 99의 visited가 1이되었는지 보면 된다.
def DFS(curr):
    visited[curr] = True

    for i in arr[curr] :
        if visited[i] == 0 : # 방문 안했으면
            DFS(i)



for _ in range(10):
    tc, road = map(int,input().split())
    arr = [[] for _ in range(100)] # 노드갯수 주어지지않았으므로 최대갯수만큼
    ls = list(map(int,input().split()))

    visited = [False] * 100
    #출발 : 0, 도착 : 99

    for i in range(road) :
        st , ed = ls[0] , ls[1] #한방향으로만 연결하므로
        del ls[0:2]
        arr[st].append(ed)

    # print(arr)
    DFS(0) #출발점이 0 이므로 0을 넘겨준다.

    if visited[99] == True :
        print('#{} 1'.format(tc))
    else :
        print('#{} 0'.format(tc))