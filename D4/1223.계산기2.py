# 문자열로 이루어진 계산식이 주어질 때, 이 계산식을 후위 표기식으로 바꾸어 계산하는 프로그램을 작성하시오.
#
# 예를 들어
#
# “3+4+5*6+7”
#
# 라는 문자열로 된 계산식을 후위 표기식으로 바꾸면 다음과 같다.
#
# "34+56*+7+"
#
# 변환된 식을 계산하면 44를 얻을 수 있다.
#
# 문자열 계산식을 구성하는 연산자는 +, * 두 종류이며 피연산자인 숫자는 0 ~ 9의 정수만 주어진다.
#
# [입력]
#
# 각 테스트 케이스의 첫 번째 줄에는 테스트 케이스의 길이가 주어진다. 그 다음 줄에 바로 테스트 케이스가 주어진다.
#
# 총 10개의 테스트 케이스가 주어진다.
#
# [출력]

# 부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 답을 출력한다.

def icp(w) : # stack에 들어오기 전 우선순위
    if w =="(" :
        return 3
    elif w == "+" or w =="-" :
        return 1
    elif w == "*" or w =="/" :
        return 2
    else :
        return -1
def isp(w) : # stack 에 들어온 후 우선순위
    if w =="(" :
        return 0
    elif w == "+" or w =="-" :
        return 1
    elif w == "*" or w =="/" :
        return 2
    else :
        return -1


for tc in range(10) :
    N = int(input())
    ls = list(input()) # 수식
    operator =['(',')','+','-','*','/']
    rear=[int(ls[0])] # 문제에서는 괄호가 없이, 첫번째 값은 무조건 값이라서 초깃값 넣어줌
    stack =[ls[1]] # 문제에서는 무조건 두번째가 수식이라서 초깃값 넣어줌
    top = 0

    # 후위표기법
    for i in range(2,N) : # 초깃값 넣어줬으므로
        if ls[i] not in operator : # 숫자면 stack에 넣지 않고, rear에 더하기
            rear.append(int(ls[i]))

        else : # 연산자일 경우
            if icp(ls[i]) > isp(stack[top]) and ls[i] != ')' :  # push할 연산자 우선순위가 더 높고, 닫는 괄호가 아니면 stack 에 쌓기
                stack.append(ls[i])
                top += 1
            else :                                              # push할 연산자 우선순위가 낮거나 같고, 닫는 괄호인 경우
                if ls[i] == ')' :                               # 닫는 괄호인 경우,
                    while stack and stack[top] != '(' :         # 여는괄호 전까지 pop
                        rear.append(stack.pop())
                        top -= 1
                    stack.pop()                                 # 닫는 괄호는 그냥 pop
                    top -= 1
                else :                                          # push할 연산자 우선순위가 낮거나 같은 경우
                    while stack and icp(ls[i]) <= isp(stack[top]) : # 우선순위가 낮거나 같으면 계속 pop
                        rear.append(stack.pop())
                        top -= 1
                    stack.append(ls[i])                             # push할 연산자 push
                    top += 1

    if len(stack) : # 스택에 남은 연산자가 있으면 pop
        for _ in range(len(stack)) : 
            rear.append(stack[top])
            top -= 1


    # 연산

    stack2=[]
    top = -1

    for i in range(len(rear)) :     # 후위 표기법으로 바꿔준 리스트 길이만큼 반복문 실행
        if type(rear[i]) == int :   # type 이 int형이면 숫자이므로 stack에 push
            stack2.append(rear[i])

        else :                      # 연산자라면, 연산 시행
            b = stack2.pop()        # 먼저 pop나온게 연산자 뒤로 가야하므로 b
            a = stack2.pop()        # 그다음 나온게 연산자 앞에 있어야하므로 a

            if rear[i] == '-' :     # 각 연산 시행
                stack2.append(a-b)
            elif rear[i] == '+' :
                stack2.append(a+b)
            elif rear[i] == '*' :
                stack2.append(a*b)
            else :
                stack2.append(a/b)

    print('#{} {}'.format(tc+1,stack2[-1])) # 가장 마지막에 남은게 연산한 값이므로 stack의 가장 마지막값(stack2[0]으로 해도 무방)을 print




