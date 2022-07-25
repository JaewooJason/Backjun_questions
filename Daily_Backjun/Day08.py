# 10952 A+B -5
while True:
    a,b = map(int,input().split())
    print(a+b)
    if a==b==0:
        break
# 밑에 있는 것이 정답!!

while 1:
    a,b = map(int,input().split())
    if (a==0) and (b==0):
        break
    else:
        print(a+b)

# 10951 문제 A+B -4 EOF관련문제 end of file
import sys

while True:
    try:
        a,b = map(int,input().split())
        # a,b = map(int,sys.stdin.readline().split())
        print(a+b)
    except:
        break

# 1110 문제 더하기 사이클

# n = int(input())
#
# while 1:

