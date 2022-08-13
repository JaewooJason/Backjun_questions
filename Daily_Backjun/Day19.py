# 2869 달팽이는 올라가고 싶다
import sys
a,b,v = map(int,sys.stdin.readline().split())
speed = (v-b)/(a-b)
print(int(speed) if speed == int(speed) else int(speed) +1)

# 다른 방식!!!
import sys
a, b, v = map(int,sys.stdin.readline().split())
print((1-(v-a)//(a-b)))

# 10250 ACM 호텔

t = int(input())

for i in range(t):
    h,w,n = map(int,input().split())
    num = (n//h) + 1
    floor = n % h
    if floor == 0:
        num -= 1
        floor = h
    print(floor*100+num)
