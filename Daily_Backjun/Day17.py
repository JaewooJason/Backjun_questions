# 2941 크로아티아 문자

croatia = ['c=','c-','dz=', 'd-', 'lj', 'nj', 's=', 'z='] # 리스트 형식으로 크로아티아 문자가 들어올때의 경우를 저장한 리스트이다.
answer = input()

for i in croatia:
    answer = answer.replace(i,'#') # 글자의 갯수를 확인하는것이기 때문에 replace 써서 하나의 문자열로 대체가 되도록 했다.
print(len(answer)) # len을 사용하여서 answer 안에 글자의 숫자를 알아냈다.

# 1316 그룹단어 체크

n = int(input())
cnt = n
for i in range(n):
    word = input()
    for j in range(len(word)-1): # 문자열은 0에서부터 시작하니까 -1을 해주는것이다.
        if word[j] == word[j+1]: # 여기는 다음 문자가 같은지를 확인 하는 코드이다.
            pass
        elif word[j] in word[j+1:]: # 여기는 같은 문자가 있으면 확인하고 카운트없애는것이다.
            cnt -=1
            break
print(cnt)
