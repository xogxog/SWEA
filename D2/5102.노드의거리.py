# 5102. [파이썬 S/W 문제해결 기본] 6일차 - 노드의 거리


def bfs(start, V) :
    q = []                  # queue로 이용
    visited = [0] * (V+1)   # 방문 체크

    q.append(start)         # q
    visited[start] = 1      # 첫번째 노드 방문체크

    while q :               # q 가 있을때 까지 돌겠다.(원하는 지점에 도착하지 않으면 알아서 종료)
        curr_node = q.pop(0)
        if curr_node == end :                       # end지점에 도착했으면
            return visited[curr_node]               # 그 지점이 start와 떨어진 정도를 return

        for i in adj_list[curr_node] :              # 현재노드에 연결된 노드들을 볼꺼다!
            if visited[i] == 0 :                    # 연결된 노드에 방문하지 않았으면,
                q.append(i)                         # i는 현재 노드의 연결된 노드이므로 바로 i를 넣어준다.
                visited[i] = visited[curr_node] + 1 # 얼마나 떨어져있는지 바로체크
    return 1

# def bfs(start,V) :
#     q = [0] * V             # queue
#     front = rear = -1
#     visited = [0] * (V + 1)
#     rear += 1
#     q[rear] = start
#     visited[start] = 1
#
#     while front != rear : # 큐가 빌때까지
#         front +=1
#         curr_node = q[front]
#
#         if curr_node == end:
#             return visited[curr_node]
#
#         for i in adj_list[curr_node] :
#             if visited[i] == 0 :
#                 rear += 1
#                 q[rear] = i
#                 visited[i] = visited[curr_node] + 1
#     return 1

T = int(input())

for tc in range(1,T+1) :
    V,E = map(int,input().split())
    adj_list = [[] for _ in range(V+1)]         # 인접 리스트

    for i in range(E) :                         # 간선 수만큼 반복
        n1,n2 = map(int,input().split())
        adj_list[n1].append(n2)                 # 양방향
        adj_list[n2].append(n1)

    start, end = map(int,input().split())       # start,end지점

    result = bfs(start,V)
    print('#{} {}'.format(tc,result-1))





