for _ in range(10) :
    tc = int(input())
    pw = list(map(int,input().split()))
    i = 1
    while True :
        minus = pw.pop(0) - i
        if minus <= 0 :
            minus = 0
            pw.append(minus)
            break
        else :
            pw.append(minus)

        i += 1                          # i 증가
        if i > 5 :                      # 사이클이 5이므로
            i = 1


    print('#{} {}'.format(tc, ' '.join(map(str,pw))))
