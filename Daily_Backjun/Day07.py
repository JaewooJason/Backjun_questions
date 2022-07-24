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
    print(' '*(star-i) +'*'*i)


# 10871 문제 X보다 작은수

import sys

n,x = map(int,sys.stdin.readline().split())
a = list(map(int,sys.stdin.readline().split()))

for i in range(n):
    if a[i] < x:
        print(a[i], end=" ")


