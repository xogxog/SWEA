T = int(input())

for tc in range(1,T+1) :
    pipes = input()

    #스택이용
    stack =[]
    top = -1

    cnt = 0 #잘린 파이프를 셀 변수

    i = 0
    while i < len(pipes) :
        #레이저를 만났을 때
        if pipes[i] == '(' and pipes[i+1] == ')' :
            if top == -1 : #지나가는 파이프가 없는 경우
                pass
            else : # 레이저 보다 앞에 파이프가 있다는 뜻이므로 잘린 파이프 세어줍니다.
                cnt += top + 1
            i += 2 #레이져 부분만큼 인덱스 이동

        #파이프 시작 부분은 스택에 넣어줍니다.
        elif pipes[i] == '(' :
            stack.append('(')
            top += 1
            i+=1

        #파이프 끝 부분은 잘려진 끝 쪽 조각 하나를 카운트하고 시작 부분을 스택에서 뺍니다.
        else :
            stack.pop()
            top -= 1
            cnt += 1
            i+=1

    print('#{} {}'.format(tc,cnt))