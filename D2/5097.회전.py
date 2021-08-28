# 5097. [파이썬 S/W 문제해결 기본] 6일차 - 회전

#queue 이용X ver.

T = int(input())

for tc in range(1,T+1) :
    N,M = map(int,input().split())
    num_ls = list(map(int,input().split()))
    i = 0
    for _ in range(M) :
        i = (i+1) % N

    print("#{} {}".format(tc,num_ls[i]))

