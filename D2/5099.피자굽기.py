# 5099. [파이썬 S/W 문제해결 기본] 6일차 - 피자 굽기

T = int(input())


for tc in range(1,T+1) :
    N, M = map(int,input().split()) # N : 화덕의 크기, M : 피자 개수
    pizza = list(map(int,input().split()))


    pizza_in =[]            # 들어가있는 피자 번호
    q = [0]*N               # queue 크기 = 화덕의 크기

    i = 0 # queue를 돌 인덱스
    j = 0 # 넣을 피자를 가리킬 인덱스

    while len(q) > 1 :
        if j<N and q[i] == 0 :          # 처음에 화덕에 넣어줄 피자
            q[i] = pizza[j]             # q에 피자넣기
            pizza_in.append(j+1)        # q에 들어간 피자번호도 카운트하기
            i = (i+1) % len(q)
            j += 1

        else :
            q[i] = q[i]//2              #치즈양 반으로 줄어듦

            if j<M and q[i] == 0 :      # 치즈가 다 녹고 새로넣을 피자가 있다면
                q[i] = pizza[j]         # 그 자리에 새로운 피자를 넣어줍니다.
                pizza_in.pop(i)
                pizza_in.insert(i,j+1)

                j += 1                  # 그 다음피자 넣을 곳을 가르켜 줍니다.
                i = (i + 1) % len(q)

            elif j>=M and q[i] == 0 :    # 더 넣을 피자가 없고, 치즈가 다 녹았다면
                q.pop(i)
                pizza_in.pop(i)
                if i == len(q) : # 빼준 자리가 마지막 자리면
                    i = 0
                else :
                    i = i

            else :
                i = (i + 1) % len(q)             # 치즈가 다 안녹거나, 그 다음피자를 넣고나서 화덕회전
            # print(f'현재가리키고있는 화덕 : {i}')

    print('#{} {}'.format(tc,pizza_in[0]))

