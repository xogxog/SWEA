#test case 8/10

T = int(input())

for t in range(T) :
    student, K = map(int,(input().split()))

    #학생들의 총점 넣은 list
    total = []
    for stu in range(student) :
        mid, fin, hw = map(int,(input().split()))
        total.append((mid * 0.35) + (fin * 0.45) + (hw * 0.2))
    
    #index값 부여
    stu_total = list(enumerate(total,1)) #index 1 부터시작
    #print(stu_total)

    #성적별 sorting
    for i in range(len(stu_total)+1) :
        for j in range(i+1,len(stu_total)) :
            #if i == len(stu_total)-1 : break
            if stu_total[i][1] < stu_total[j][1] :
                stu_total[i], stu_total[j] = stu_total[j], stu_total[i]

        #print(stu_total)
    
    for stu in range(len(stu_total)) : 
        if stu_total[stu][0] == K :
            rank = (stu+1) / student
            if rank <= 0.1 :
                print(f'#{t+1} A+') 
                break
            elif rank <=0.2 :
                print(f'#{t+1} AO')
                break
            elif rank <=0.3 :
                print(f'#{t+1} A-')
                break
            elif rank <=0.4 :
                print(f'#{t+1} B+')
                break
            elif rank <=0.5 :
                print(f'#{t+1} BO')
                break
            elif rank <=0.6 :
                print(f'#{t+1} B-')
                break
            elif rank <=0.7 :
                print(f'#{t+1} C+')
                break
            elif rank <=0.8 :
                print(f'#{t+1} CO')
                break
            elif rank <=0.9 :
                print(f'#{t+1} C-')
                break
            else : 
                print(f'#{t+1} DO')
                break
            #print(stu_total[stu][0])

    
    