T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    pizza = list(map(int, input().split()))

    pizza = [[idx, cheeze] for idx, cheeze in enumerate(pizza)] #이걸 이렇게 할 수 있군...

    oven = []
    for _ in range(N):
        oven += [pizza.pop(0)]

    wait = pizza

    while len(oven) > 1:
        oven_i, oven_p = oven.pop(0)
        oven_p = oven_p // 2

        if oven_p != 0:
            oven.append([oven_i, oven_p])

        elif oven_p == 0:
            if len(wait) > 0:
                oven.append(wait.pop(0))

    print('#{} {}'.format(tc, oven[0][0] + 1))