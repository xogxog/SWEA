T = int(input())

for t in range(T) :
    commend_N = int(input())
    drive=[]
    for N in range(commend_N) :
        drive.append(list(map(int, input().split())))
    
    #print(drive)
    velocity = 0 #속도
    distance = 0 # 거리
    for d in range(len(drive)) :
        #전진!
        if drive[d][0] == 1 :
            velocity += drive[d][1]
            distance += velocity
            #print(distance)

        #후진!
        elif drive[d][0] == 2 :
            #속도가 0이거나 그것보다 작으면 속도 =0
            if velocity - drive[d][1] < 0 :
                velocity = 0
                continue
            #속도 0 이상이면 감속
            velocity -= drive[d][1]
            distance += velocity
        
        # 유지!
        elif drive[d][0] == 0 :
            distance += velocity
    
    print(f'#{t+1} {distance}')