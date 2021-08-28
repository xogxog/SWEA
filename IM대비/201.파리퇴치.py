T = int(input())

def sub_tot(ls) :
    tot = 0
    for i in range(len(ls)) :
        for j in range(len(ls)) :
            tot += ls[i][j]
    return tot




for tc in range(1,T+1) :
    N,M = map(int,input().split())
    room = [list(map(int,input().split())) for _ in range(N)]
    max_tot = 0
    for i in range(N-M+1):
        for j in range(N-M+1) :
            die = [r[j:j+M] for r in room[i:i+M]]
            tot = sub_tot(die)
            if max_tot < tot :
                max_tot = tot
    print('#{} {}'.format(tc, max_tot))