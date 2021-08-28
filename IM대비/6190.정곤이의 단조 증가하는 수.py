
T = int(input())

def jung_rule(arr) :
    # print(arr)
    max_num = -1
    for i in range(len(arr)-1) :
        for j in range(i+1, len(arr)) :
            flag = 0
            gob = str(int(arr[i]) * int(arr[j]))
            # print(gob)
            if len(gob) >1 :
                for m in range(len(gob)-1) :
                    if gob[m] > gob[m+1]:
                        flag = 1
                        break
            if flag == 0 and max_num < int(gob) :
                # print(max_num)
                max_num = int(gob)

    return max_num



for tc in range(1,T+1) :

    N = int(input())
    numbers = input().split()

    result = jung_rule(numbers)

    print('#{} {}'.format(tc, result))