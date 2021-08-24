# 2070. 큰 놈, 작은 놈, 같은 놈

T = int(input())
number =[]

for i in range(0,T) :    
    number.append(list(map(int, input().split(' '))))
    #a,b=map(int, input().split(' '))
#print(number)

i=1
for num in number :

    print(f'#{i} ',end='')
    if num[0] > num[1] :
        print('>')
    elif num[0] < num[1] :
        print('<')
    else :
        print('=')
    i+=1




# input 받아오는게 힘이 좀 들었다....








