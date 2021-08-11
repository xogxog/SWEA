
T=int(input())

for tc in range(1,T+1) :
    card_N = int(input())
    cards= input()
    cards_ls =[0] * 10

    for n in cards :
        cards_ls[int(cards) % 10] += 1
        cards = int(cards) // 10
    #print(cards_ls)

    max_cnt = 0
    max_idx =0
    for idx in range(len(cards_ls)) :
        #print(idx)
        if max_cnt <= cards_ls[idx] :
            max_cnt = cards_ls[idx]
            max_idx = idx
        # elif max_cnt == cards_ls[idx] : #위에 등호가 있으면 이 문장은 필요가 없다.
        #     max_idx = idx

    print('#{} {} {}'.format(tc, max_idx, max_cnt))