# 1989. 초심자의 회문 검사 

n = int(input()) # 몇개 받을 지
words =[]
for i in range(n) :
    words.append(input())

#print(words)


def palindrome(word) :
    # 중간까지 왔으면 return 1
    if len(word) <= 1 : 
        return 1
    #회문
    if word[0] == word[-1] :
        return palindrome(word[1:-1])
    else : return 0


# enumerate()

for word in words :
    #print(f'#{words.index(word)+1} {palindrome(word)}')
    print('#{0} {1}'.format(words.index(word)+1, palindrome(word))) #1 
