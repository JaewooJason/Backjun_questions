# 2439 문제 별찍기 -2

star = int(input())
num = 0

for i in range(1,star+1):
    num +=1
    print(' '*num,'*'*star)
# 정답은 이거다
''' 여기서 이해해야하는것은 14번째 줄의 코드이다. 먼저 입력받은 숫자를 -i를 해줌으로써 입력받은 n의 칸에 *이 추가된다고 생각하면된다.'''
star = int(input())

for i in range(1,star+1):
    print(' '*(star-i) +'*'*i) # range를 통해서 1에서부터 +1까지 돌기 때문에 변수로 받은 star에서 ' '* -i을 해주고 '*'*i해주면 된다.


# 10871 문제 X보다 작은수

import sys

n,x = map(int,sys.stdin.readline().split())
a = list(map(int,sys.stdin.readline().split()))

for i in range(n):
    if a[i] < x:
        print(a[i], end=" ")


# 1526 문제 가장 큰 금민수

n = int(input())

while True:
    flag = True
    for i in str(n):
        if i != '4' and i != '7': # 문자열로 바꾸는 이유는 하나하나 비교를 하기 위해서이다. 4와 7이 들어있나를 확인하기 위해서 하나하나 확인하기 때문에 100이 경우 -1 세번 이루어지기 때문에 다음문자는 97이 되는것이다.
            flag = False # 여기서 하나라도 False 이면 정답이 아니기 때문에 답이 아니다.
            n -= 1
    if flag:
        print(n)
        break


