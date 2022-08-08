# 1152 단어의 개수

n = input().split()
print(len(n))


# 상수
# 이 문제에서 중요한것은 숫자를 역순으로 바꾸는것이다.
a, b  = input().split()
a = int(a[::-1]) # 이렇게 슬라이싱을 이용하면 들어온 숫자를 역순으로 변경할 수 있다.
b= int(b[::-1])

if a > b:
    print(a)
else:
    print(b)

# 5622 문제 다이얼

dial = ['ABC','DEF', 'GHI','JKL','MNO','PQRS','TUV', 'WXYZ']

num = list(input())

time = 0

for i in num:
    for j in dial:
        if i in j :
            time += dial.index(j) + 3 # 항상주의 메세드를 사용할때에는 []가 아니라 ()이다!!!!
print(time)