# 1860. 진기의 최고급 붕어빵
# 출력 첫단어 대문자아니여서 틀렸...ㅎㅎ
# 반복문 조건 줄때 꼼꼼히 빼먹지 말고 주기
T = int(input())


def po_or_imp():
    global flag
    cnt = 0
    i = 0
    for time in range(ppl[-1] + 1):
        if time != 0 and time % M == 0:
            cnt += K

        if ppl[i] == time:
            while i < len(ppl) and ppl[i] == time:
                cnt -= 1
                i += 1

        if cnt < 0:
            return 'Impossible'
    return 'Possible'


for tc in range(1, T + 1):
    N, M, K = map(int, input().split())  # N : 붕어빵먹을 수 있는 사람, M : 0~M초 , K : M초간 k개 붕어빵
    flag = 0
    # 붕어빵먹을 수 있는사람 도착시간
    ppl = list(map(int, input().split()))
    ppl.sort()

    result = po_or_imp()
    print('#{} {}'.format(tc, result))
