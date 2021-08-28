T = int(input())

#입력
for t in range(0, T) :
    N = int(input()) 
    array = {}
    for n in range(0, N) :
        alpha, num = map(str, input().split())
        array[alpha] = int(num)
    #print(array)

# 출력할 알파벳 리스트로 받아오기
    alpha_ls = []
    for key,value in array.items() :
        #print(key,value)
        for i in range(value) :
            alpha_ls.append(key)
    #print(alpha_ls)
        
    print(f'#{t+1}')
    while len(alpha_ls) > 0 : #23
        print(''.join(alpha_ls[0:10]))
        del alpha_ls[0:10] #pop과 del의 차이 : pop은 지정해주지 않거나, 하나만 가능, del은 slicing 이용한 삭제 가능
        print(alpha_ls)
    #print("",end ='')


#어려웠던 점
# 1. 처음에 N 과 array를 가장 밖에 둬서 test case가 여러개인경우 array가 중복 되서 그런지 정답이 맞지 않았다.
# 2. alpha_ls로 모든 알파벳을 받는건