# 1
# 10
# 1 2 3 2 4 6 4 2 1 3


T = int(input())

# 가장 큰 값의 인덱스를 찾을 건데 앞에있는 큰값의 인덱스를 찾아야 하므로 거꾸로 탐색
def Mymax(ls) :
    my_max = 0 #가장 큰 값을 담는 변수
    my_max_idx = 0 #가장 큰 값의 인덱스를 담는 변수
    for i in range(len(ls)-1,-1,-1) :
        if my_max < ls[i] :
            my_max = ls[i]
            my_max_idx = i
    return my_max_idx


for tc in range(0,T) :
    N = int(input()) #연속된 N일 동안의 물건의 매매가를 예측하여 알고 있다.
    future = list(map(int,input().split())) # 1 2 3 2 4 6 4 2 1 3
    #print(future)
    cut_ls=[]

    revenue = 0 # 이익 변수

    while len(future) > 0 :
        max_idx = Mymax(future)
        cut_ls = future[0:max_idx+1] #가장 큰값을 가진날 까지 인덱스 자름.

        if len(cut_ls) == 1: # 가장 큰값만 뽑혔다는 말은, 이때 가격보다 낮았던 날이 없었다는 뜻이므로 그냥 삭제한다.
            del future[0]

        else : # len(cut_ls) 가 1보다 큰 수가 나왔다는 것은 최고가보다 금액이 낮았던 날이 있었다는 의미
            for i in range(0,len(cut_ls)) :
                revenue += (cut_ls[-1]-cut_ls[i]) # 최고가전까지 샀던 물건들 이익 합
            del future[0:max_idx+1] # 잘라준다.

    print('#{} {}'.format(tc+1,revenue))







