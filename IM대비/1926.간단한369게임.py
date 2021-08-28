
N = int(input())

for i in range(1,N+1) :
    cnt = 0
    num = i
    # print(num, cnt)
    while num>0 :
        if num % 10 == 3 or num % 10 == 6 or num % 10 == 9 :
            cnt += 1
        num //= 10
        # print(num,cnt)
    if cnt == 0 :
        print('{} '.format(i),end='')
    else :
        print('{} '.format('-'*cnt),end='')

