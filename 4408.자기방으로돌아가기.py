# 각 끝값이 시작값보다 작으면 된다.

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    run_stu = [list(map(int, input().split())) for _ in range(N)]

    # 홀수 관계없이 하기위해 index기준으로 모두 바꿔줌
    for i in range(N):
        for j in range(2):
            if run_stu[i][0] > run_stu[i][1]:  # 숫자 오름차순으로 정렬
                run_stu[i][0], run_stu[i][1] = run_stu[i][1], run_stu[i][0]

            if run_stu[i][j] % 2:  # 홀수방인 경우
                run_stu[i][j] = int((run_stu[i][j] // 2))
            else: #짝수 방인경우
                run_stu[i][j] = int((run_stu[i][j] / 2) - 1)

    cnt = [0] * 201 #0번 방은 없으므로 201개를 만들어준다.

    # 걸리는 시간은 곧, 동선이 겹치는 것 중 가장 큰 값을 의미한다.
    # print(run_stu)
    for i in range(N):
        for j in range(run_stu[i][0], run_stu[i][1]+1) :
            cnt[j] += 1

    #지나간 동선중 가장 큰 값 찾기
    cnt_max = 0
    for i in range(len(cnt)):
        if cnt_max < cnt[i] :
            cnt_max = cnt[i]



    print('#{} {}'.format(tc, cnt_max))