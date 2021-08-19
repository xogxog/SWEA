T = int(input())

def fact(n) :
    if n <= 1:
        return 1
    return n * fact(n-1)


for tc in range(1,T+1) :

    N = int(input())

    #세로는 길이 20으로 고정이므로 가로만 가지고 모든 경우의 수를 먼저 구한다.
    #길이가 10인 경우의 수를 구한다.

    cases = [] # 가로길이로만 구한 경우의 수
    curr_case =[] # 현재의 경우의 수

    # 길이가 10인 테이프만 붙였을 때
    while N > 1 :
        N -= 10
        curr_case.append(1)


    cases.append(curr_case[:]) # 경우의 수 추가

    # 가로로만 놓았을 때 [1,1,1] [1,2]
    i = 0
    while True :

        if len(curr_case) == 1:
            break

        elif curr_case[i] == 1 and curr_case[i+1] == 1 : # i번째와 i+1번째가 1이면
            del curr_case[i:i+2] # 삭제하고
            curr_case.append(2) # 길이가 2인 테이프로 갈아끼운다.
            cases.append(curr_case[:])

        else :
            break



    cnt = 0 #모든 경우의 수 카운트

    for i in range(len(cases)) :
        cnt_A = 0  # 길이가 10인테이프 갯수
        cnt_B = 0  # 길이가 20인 테이프 갯수
        for j in range(len(cases[i])) :
            if cases[i][j] == 1 :
                cnt_A += 1
            else :
                cnt_B += 1
        # print(cnt_A, cnt_B)
        if cnt_A == len(cases[i]):
            cnt += 1
            # print(cnt)

        else :
            cnt += (fact(len(cases[i])) / (fact(cnt_A) * fact(cnt_B))) * (2 **(cnt_B))
            # print(cnt)



    print('#{} {}'.format(tc,int(cnt)))





