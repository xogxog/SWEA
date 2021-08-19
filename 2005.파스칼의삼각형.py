T = int(input())

for tc in range(1,T+1):
    N = int(input())
    pascal = [[0] * i for i in range(1,N+1)] #배열 먼저 만들어 준다.

    for i in range(N) :
        for j in range(i+1) :
            #양끝값은 항상 1로 준다.
            if j == 0 or j == i :
                pascal[i][j] = 1
            # 양 끝값이 아닌경우, 파스칼법칙에 의해 자기왼쪽위+자기오른쪽위
            else :
                pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]

    print('#{}'.format(tc))

    for p in range(N):
        for q in range(p + 1):
            print('{}'.format(pascal[p][q]) , end=' ')
        print('')