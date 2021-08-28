def change(arr):
    result = ''
    for w_1 in arr:
        if w_1 in one_w:
            result += '1'
        elif w_1 in two_w:
            result += '2'
        elif w_1 in three_w:
            result += '3'

    return result


T = int(input())

for tc in range(1, T + 1):
    word_1, word_2 = input().split()
    one_w = 'CEFGHIJKLMNSTUVWXYZ'
    two_w = 'ADOPQR'
    three_w = 'B'

    change_w_1 = change(word_1)
    change_w_2 = change(word_2)

    if change_w_1 == change_w_2:
        print('#{} {}'.format(tc, 'SAME'))
    else:
        print('#{} {}'.format(tc, 'DIFF'))
