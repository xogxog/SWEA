#1926. 간단한 369게임



three_six_nine = ['3','6','9']
N = int(input())

for number in range(1,N+1) : #1~N까지

    number = str(number) # str형으로 바꿔줌 
    cnt = 0 # '-'를 몇개 출력할지 세어주는 친구
    
    for num in number : # 숫자 하나하나 판별하기위한 이중 for문    
        if num in three_six_nine :
            cnt += 1
           

    if cnt > 0 : 
        print(('-' * cnt) + ' ', end ='')
    else : 
        print(number, end =' ')





    #print(type(number))


#힘들었던 점.
# cnt를 자꾸 이중 for문안에 넣어줘서 초기화되서 값이 제대로 나오지 않음.
