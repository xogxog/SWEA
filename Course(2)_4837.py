#4837. [파이썬 S/W 문제해결 기본] 2일차 - 부분집합의 합

#비트연산자

T = int(input())

for tc in range(1,T+1) :
    # N : 원소의 수
    # K : 부분집합의 합
    N,K = map(int,input().split())
    arr = [1,2,3,4,5,6,7,8,9,10,11,12]

    n = len(arr)
    cnt = 0

    sub =[]
    for i in range(1 << n): # 모든 경우의 수
        curr_sub = []
        for j in range(n):
            if i & (1 << j):
                curr_sub.append(arr[j])
                #print(curr_sub)
        if len(curr_sub) == N:
            sub.append(curr_sub)
    #print(sub)


    for i in range(len(sub)) :
        curr_sum = 0
        for j in range(len(sub[i])):
            curr_sum += sub[i][j]
        if curr_sum == K :
            cnt += 1

    print('#{} {}'.format(tc, cnt))