#0~9 사이의 숫자카드에서 임의의 카드 6장을 뽑았을 때, 3장의 카드가 연속적인 번호를 갖는 경우를 run이라 하고,
# 3장의 카드가 동일한 번호를 갖는 경우를 triplet이라고 한다.
#
# 그리고 6장의 카드가 run과 triplet으로만 구성된 경우를 baby-gin으로 부른다.
#
# 6자리의 숫자를 입력을 받아 baby-gin 여부를 판단하는 프로그램을 작성하라.
#
# 베이비진이 맞다면 1을 아니라면 0을 출려하여라...
#
# 입력
#
# 첫줄에는 테스트케이스 개수가 주어지고, 이후 6장의 카드가 주어진다.
#
# 출력
#
# #(테케번호) (정답) 형식으로 출력할것.

T=int(input())

#재귀함수 쓰는게 굉장히 힘이들었다.....
def My_triplet(ls) :
    triplet = 0
    for i in range(10):
        if ls[i] >= 3:
            ls[i] -= 3
            triplet += 1
            if ls[i]>=3 : triplet+= My_triplet(ls)
    return triplet

def My_baby_run(ls) :
    baby_run =0
    for i in range(0,8):
        if ls[i] >=1 and ls[i+1]>=1 and ls[i+2]>=1 :
            ls[i] -=1
            ls[i+1] -=1
            ls[i+2] -=1
            baby_run+=1
            if ls[i] >=1 and ls[i+1]>=1 and ls[i+2]>=1 : baby_run+=My_baby_run(ls)
    return baby_run

for tc in range(T) :
    ls=[0] * 10
    N=input() #int형으로 받으면 앞에숫자 0이 사라진다.
    for i in range(6):
        ls[int(N)%10] += 1
        N = int(N) // 10
    #print(ls)

    triplet, baby_run = 0,0

    My_triplet(ls)
    My_baby_run(ls)
    #print(ls)
    check_baby_gin =0
    for i in ls :
        check_baby_gin += ls[i]

    if check_baby_gin ==0 :print('#{} {}'.format(tc+1, 1))
    else :print('#{} {}'.format(tc+1, 0))


