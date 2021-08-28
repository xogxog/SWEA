
"""
1
9
XXXXXXXXX
XXXHXXXXX
XXHAHXXHX
XXHHXXXXX
XXXXXXXXX
XXAHHXXXX
XXHXXHAHX
XXAHXXHXX
XXHXHXXXX


2
9
XXXXXXXXX
XXXHXXXXX
XXHAHXXHX
XXHHXXXXX
XXXXXXXXX
XXAHHXXXX
XXHXXHAHX
XXAHXXHXX
XXHXHXXXX
12
XXXHXXXXXXXA
XXXHXXXXXXXX
XXHHHXXXXXXX
XXXBHHXXXAXX
XXXXXXXHXHXX
XXXHXXHXXXXX
XXXXXXXXXXXX
XXXXHXXHXXXX
XXXXXXXCHXXH
XXHXXXHHXXXX
XXXXXXXXXXXX
BHXXXXXHXXXX

"""


T = int(input())

for tc in range(1,T+1) :
    N = int(input()) #배열의 갯수
    home = list((list(input()) for _ in range(N)))
    for _cc in range(N):
        print(*home[_cc])
    print("------------------")

    A_rc = [(1,0),(-1,0),(0,1),(0,-1)]
    B_rc = [(1,0),(-1,0),(0,1),(0,-1),(2,0),(-2,0),(0,2),(0,-2)]
    C_rc = [(1,0),(-1,0),(0,1),(0,-1),(2,0),(-2,0),(0,2),(0,-2),(3,0),(-3,0),(0,3),(0,-3)]

    for i in range(N) :
        for j in range(N):
            if home[i][j] =='A':
                for m in range(len(A_rc)) :
                    a_r = i + A_rc[m][0]
                    a_c = j + A_rc[m][1]
                    if 0<= a_r <N and 0<= a_c <N :
                        home[a_r][a_c] = 'X'

            elif home[i][j] =='B':
                for n in range(len(B_rc)) :
                    b_r = i + B_rc[n][0]
                    b_c = j + B_rc[n][1]
                    if 0<= b_r <N and 0<= b_c <N :
                        home[b_r][b_c] = 'X'
            elif home[i][j] =='C' :
                for p in range(len(C_rc)) :
                    c_r = i + C_rc[p][0]
                    c_c = j + C_rc[p][1]
                    if 0<= c_r <N and 0<= c_c <N :
                        home[c_r][c_c] = 'X'

    result = 0
    for _ in range(N) :
        result += home[_].count('H')


    print(result)