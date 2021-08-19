T = int(input())





for tc in range(1,T+1) :
    words = input()

    stack=[]
    top = -1


    for i in range(len(words)) :

        if top == -1 :
            top += 1
            stack.append(words[i])

        else :
            if words[i] == stack[top] :
                stack.pop()
                top -= 1

            else :
                stack.append(words[i])
                top += 1


    print('#{} {}'.format(tc,len(stack)))

