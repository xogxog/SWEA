T = int(input())

for tc in range(1,T+1) :

    N = int(input())
    ls = input().split()

    if N % 2 : #홀수이면
        middle = (N+1) // 2
    else : #짝수이면
        middle = N//2

    left_ls = ls[: middle]
    right_ls = ls[middle:]

    new_ls =[]
    for i in range(N) :
        if i % 2 : # 홀수이면
            new_ls.append(right_ls[i//2])
        else :
            new_ls.append(left_ls[i//2])

    print('#{} {}'.format(tc, ' '.join(new_ls)))
