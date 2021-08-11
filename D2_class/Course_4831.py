#전기버스
#A도시는 전기버스를 운행하려고 한다. 전기버스는 한번 충전으로 이동할 수 있는 정류장 수가 정해져 있어서, 중간에 충전기가 설치된 정류장을 만들기로 했다.
#
# 버스는 0번에서 출발해 종점인 N번 정류장까지 이동하고, 한번 충전으로 최대한 이동할 수 있는 정류장 수 K가 정해져 있다.
#
# 충전기가 설치된 M개의 정류장 번호가 주어질 때, 최소한 몇 번의 충전을 해야 종점에 도착할 수 있는지 출력하는 프로그램을 만드시오.
#
# 만약 충전기 설치가 잘못되어 종점에 도착할 수 없는 경우는 0을 출력한다. 출발지에는 항상 충전기가 설치되어 있지만 충전횟수에는 포함하지 않는다.

# 첫 줄에 노선 수 T가 주어진다.  ( 1 ≤ T ≤ 50 )
# 각 노선별로 K, N, M이 주어지고, 다음줄에 M개의 정류장 번호가 주어진다. ( 1 ≤ K, N, M ≤ 100 )
# 최대 K번 이동가능, 종점인 정류장 :N 번, 충전기가 설치된 : M개 정류장 번호

T=int(input())

for tc in range(T) :
    K,N,M = map(int, input().split())
    bus_stop =[0] *(N+1)
    charger_ls = [int(i) for i in input().split()]

    # 충전가능한 bus_stop 표시
    for idx in charger_ls:
        bus_stop[idx] += 1

    bus_loca =0
    k = 0 # k번이동하시오

    #버스 도착하면 멈추시오
    charge_num = 0 #충전횟수
    while bus_loca < N :
        k = 0  # k번이동하시오
        curr_charger_ls = []
        for idx in range(bus_loca+1 ,len(bus_stop)) :
            if bus_stop[idx] == 1 :
                curr_charger_ls.append(idx)
            k +=1
            if k == K : break

        # 이동가능거리안에 충전기가 없으면 종료
        if len(curr_charger_ls) == 0 :
            print('#{} {}'.format(tc+1, 0))
            break

        #이동거리안에 충전기가 있는경우
       else :
            bus_loca = curr_charger_ls[-1]
            charge_num += 1

            if bus_loca + K >= N : #도착하면 끝내세요!
                bus_loca += K
                print('#{} {}'.format(tc + 1, charge_num))





