#숫자를 정렬하자.
# 주어진 N 길이의 숫자열을 오름차순으로 정렬하여 출력하라.
#
# [제약 사항]
#
# N 은 5 이상 50 이하이다.
#
# [입력]
#
# 가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
# 각 테스트 케이스의 첫 번째 줄에 N 이 주어지고, 다음 줄에 N 개의 숫자가 주어진다.
#
# [출력]
#
# 출력의 각 줄은 '#t'로 시작하고, 공백을 한 칸 둔 다음 정답을 출력한다.
# (t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)

T = int(input())

for tc in range(1,T+1) :
    N = int(input())
    ls = list(map(int, input().split()))

    for stan_idx in range(N-1) :
        min_idx = stan_idx # 기준 idx 를 최소값idx 넣을 변수에 넣어준다.
        for comp_idx in range(stan_idx+1, N) :
            if ls[min_idx] > ls[comp_idx] : # 찾은 값이 기준값보다 작으면
                min_idx = comp_idx #최소값을 가진 index를 min_idx에 넣어준다.
        ls[stan_idx], ls[min_idx] = ls[min_idx], ls[stan_idx] #최소값과 기준값 swap

    print('#{} {}'.format(tc, ' '.join(map(str,ls)))) # ls안에는 int형이므로 join을 위해 str형으로 바꿔 준후에 join함수 적용
    #print(*ls)