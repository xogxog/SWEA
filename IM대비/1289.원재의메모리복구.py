T = int(input())


for tc in range(1,T+1):
    ls = list(input())
    cnt = 0
    p = '0'
    if ls[0] == '1' :
        cnt+=1
        p = '1'
    for i in range(1,len(ls)) :
        if p != ls[i] :
            cnt += 1
            p = ls[i]

    print('#{} {}'.format(tc,cnt))