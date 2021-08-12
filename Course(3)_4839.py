T = int(input())

def search_page(book_page,key) :
    start = 0
    end = len(book_page) - 1
    cnt = 0
    while start <= end:
        middle = (start + end) // 2  # 길이 짝, 홀 상관없다.
        if book_page[middle] == key:  # 검색성공
            cnt += 1
            return cnt
        elif book_page[middle] > key: # 찾는 쪽수가 중간 값 보다 작은 경우
            cnt += 1
            end = middle #문제 잘읽자!!!!!여기 문제에서는 middle값으로 설정해준다.
        else:
            cnt += 1
            start = middle


for tc in range(1,T+1) :

    P, A_key, B_key = map(int,input().split())
    #print(P,A_key,B_key)
    book_page = [i for i in range(1,P+1)]

    A = search_page(book_page,A_key)
    B = search_page(book_page,B_key)

    if A > B :
        print('#{} B'.format(tc))
    elif A < B :
        print('#{} A'.format(tc))
    else :
        print('#{} 0'.format(tc))
