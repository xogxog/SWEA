#1대1 가위바위보
# A와 B가 가위바위보를 하였다.
#
# 가위는 1, 바위는 2, 보는 3으로 표현되며 A와 B가 무엇을 냈는지 입력으로 주어진다.
#
# A와 B중에 누가 이겼는지 판별해보자. 단, 비기는 경우는 없다.

ls = input().split()

if ls[0] == 1 and ls[1]==2 : print('B')
elif ls[0] == 2 and ls[1]==3 : print('B')
elif ls[0] == 3 and ls[1]==1 : print('B')
else : print('A')