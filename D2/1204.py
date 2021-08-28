# 최빈 수 구하기

# runtime error

T = int(input())

for t in range(T) :
    test_case = int(input())
    scores = list(map(int, input().split())) #리스트로 저장
    print(scores)
    
    
    key =set(scores) # score을 key로
    score_dic = {} # 점수별 갯수 카운트
    for score in key :
        score_dic[score] = scores.count(score)


    mode_num = 0
    for num in score_dic.values() :
        if mode_num < num : mode_num = num # 최빈수 저장
    

    max_mode_numbers = [] # 최빈수가 여러개인 경우, 최빈값을 가지는 수들을 저장하기 위함.
    for sco in score_dic.keys() :
        if score_dic[sco] == mode_num :
            max_mode_numbers.append(sco)
    print(f'#{test_case} {max(max_mode_numbers)}')
    

    # cnt = 0
    # mode_score = 0
    # for num in range(101) : # 100점 까지만 존재하므로
    #     if scores.count(num) >= cnt :
    #         cnt = scores.count(num)
    #         mode_score = num    
    # print(f'#{test_case} {mode_score}')