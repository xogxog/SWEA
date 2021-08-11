#min,max 출력
T=int(input())

for tc in range(T):
    N= int(input())
    Num_ls = [int(i) for i in input().split()]

    max_num = Num_ls[0]
    min_num= Num_ls[0]
    for n in Num_ls :
        if max_num < n :
            max_num = n
        if min_num > n :
            min_num =n

    print('#{} {}'.format(tc+1, max_num-min_num))