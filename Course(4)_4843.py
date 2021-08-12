T=int(input())

for tc in range(1, T+1):
    N = int(input())
    ls = list(map(int,input().split()))

    max_flag = 0 # 큰 값을 가진 인덱스 넣어줄 곳
    min_flag = 0 # 작은 값을 가진 인덱스 넣어줄 곳

    for i in range(len(ls)-1) :
        max_flag = i  # 큰 값을 가진 인덱스 넣어줄 곳
        min_flag = i # 작은 값을 가진 인덱스 넣어줄 곳
        if i % 2 == 0 : # idx가 짝인 곳에 큰값을 넣어주므로
            for j in range(i+1, len(ls)):
                if ls[max_flag] < ls[j] :
                    max_flag = j
            ls[i],ls[max_flag] = ls[max_flag],ls[i]
        else : #idx가 짝인 곳에 작은 값을 넣어주므로
            for k in range(i+1, len(ls)):
                if ls[min_flag] > ls[k] :
                    min_flag = k
            ls[i],ls[min_flag] = ls[min_flag],ls[i]


    print('#{} {}'.format(tc,' '.join(map(str, ls[0:10]))))