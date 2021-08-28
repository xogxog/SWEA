# 값을 넣은 후에, curr-1 처리해주는게 헷갈려서 오래걸렸다.
def DFS(S,G) :
    stack =[]
    stack.append(S)

    while stack : #스택이 공백일때까지 도는 것이니까(처음 st값을 넣어줘서 반복문 실행이 되는것이다.)
        curr = stack.pop()
        # print(curr)

        if curr == G :
            return 1

        if not visited[curr-1] : # 방문하지 않았다면
            visited[curr-1] = True #방문처리

            for i in range(V) :
                if adj_arr[curr-1][i] and not visited[i] : #인접해있고 방문하지 않았으면
                    stack.append(i+1)

    return 0






T = int(input())

for tc in range(T):

    V,E = map(int, input().split())

    adj_arr = [[0]*(V) for _ in range(V)]
    visited = [False] * (V)
    for i in range(E) :
        st, ed = map(int, input().split())
        adj_arr[st-1][ed-1] = 1 # 여기서 끝내면 방향성이 있는 그래프
    # print(adj_arr)


    S,G = map(int, input().split())




    result = DFS(S,G)
    print('#{} {}'.format(tc+1,result))

