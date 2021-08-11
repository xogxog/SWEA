T=int(input())

for tc in range(T):
    N=int(input())
    ls = [int(i) for i in input().split()] #list(map(int, input().split()))
    #print(ls)

    max_count=0 #떨어지는 높이가 max인 값 넣을 변수
    for i in range(len(ls)-1) :
        cnt =0 #떨어지는 횟수
        for j in range(i+1,len(ls)) :
            if ls[i] > ls[j] : #오른쪽에있는 박스가 왼쪽의 박스길이보다 작으면 떨어지므로
                cnt +=1 #count +1
        if max_count < cnt :
            max_count = cnt

    print('#{} {}'.format(tc+1, max_count))

