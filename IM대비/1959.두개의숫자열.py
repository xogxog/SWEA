T = int(input())


def my_multi(arr1,arr2,m,n) : # arr1이 짧음
    max_tot = -1000000
    for i in range(n-m+1) :
        tot = 0
        for j in range(i, i+m) :
            _multi = arr1[j-i] * arr2[j]
            tot += _multi
        if max_tot < tot :
            max_tot = tot

    return max_tot

for tc in range(1,T+1) :
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))

    if N<M :
        result = my_multi(A,B,N,M) # a 가 짧음
    else :
        result = my_multi(B,A,M,N)

    print('#{} {}'.format(tc,result))