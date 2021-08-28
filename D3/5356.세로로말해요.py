T= int(input())


for tc in range(1,T+1):
    words = [input() for _ in range(5)]

    # 최고길이 문자열 찾기
    word_max = 0
    for word in words:
        if word_max < len(word) :
            word_max = len(word)


    # 없는 단어 !로 채워줌
    for i in range(0,len(words)) :
        if len(words[i]) < word_max :
            words[i] = words[i] + ('!'*(word_max-len(words[i])))


    #세로로 읽기
    result =''
    for i in range(0, word_max):
        for j in range(0,len(words)) :
            if words[j][i] =='!' :
                continue
            else :
                result+=words[j][i]

    print('#{} {}'.format(tc,result))