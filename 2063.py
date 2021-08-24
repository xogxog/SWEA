import random

def median(n):
    #난수 생성 후, 저장하는 문장
    N = []
    for i in range(0,n) :
        rand_N = random.randrange(1,200) #1이상 200미만의 수를 가지는 난수
        N.append(rand_N)
    
    #random.randint(1,201,n)
    
    #정렬하는 함수 sorted
    '''
    sorted_n_list = sorted(N)
    print(sorted_n_list[len(N)//2])
    '''
    #순서대로 sorting


    for i in range(0,len(N)) : # 기준 인자
        for j in range( i+1, len(N)) : #비교해줄 인자
            if N[i] > N [j] : # 기준인자보다 비교할 인자가 크면
                N[i] , N [j] = N[j] , N [i] #스왑
                print(N) # 정렬 잘 됐는지 확인 용
    return(N[len(N)//2]) 
                




n = int(input())
 # 1~199까지의 난수 생성

print(median(n))