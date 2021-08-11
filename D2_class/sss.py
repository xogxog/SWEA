def My_max_num(nums):
    max_num = nums[0]
    for num in nums:
        if max_num <= num:
            max_num = num
    return max_num

def My_min_num(nums):
    min_num = nums[0]
    for num in nums:
        if min_num >= num:
            min_num = num
    return min_num

for tc in range(1, 11): #총 10개 test 케이스
    dump = int(input())
    box_height = list(map(int, input().split()))
    cnt_dump = 0

    # 정해진 dump 횟수와 실행된 dump 횟수가 같을때 까지 실행
    while cnt_dump < dump:
        for j in range(len(box_height)): #box 인덱스
            if My_max_num(box_height) == box_height[j]:
                box_height[j] -= 1 #가장 높은 box를 하나 빼고
                break
        for k in range(len(box_height)): #box 인덱스
            if My_min_num(box_height) == box_height[k]:
                #and My_max_num(box_height) == box_height[j]
                box_height[k] += 1 #가장 낲은 box를 하나 더 한다.
                #box_height[j] -= 1
                cnt_dump += 1 #dump 실행 누적
                break

    print('#{} {}'.format(tc, My_max_num(box_height) - My_min_num(box_height)))