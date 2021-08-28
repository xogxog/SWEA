T = int(input())

def mystack(words) :

    stack = []
    top = -1

    for word in words:
        if word == '(' or word == '{':
            top += 1
            stack.append(word)
            # print(stack)

        elif stack and word ==')' :
            if stack[top] == '(':
                stack.pop()
                top -= 1
                # print(stack)
            else : return 0

        elif stack and word == '}' :
            if stack[top] == '{':
                stack.pop()
                top -= 1
                # print(stack)
            else : return 0

        elif word ==')' or word == '}' and top == -1 :
            return 0



    if top == -1 :
        return 1
    else : return 0



for tc in range(1, T+1):
    words = input()
    result = mystack(words)

    print('#{} {}'.format(tc,result))


