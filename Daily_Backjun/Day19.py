# 2869 달팽이는 올라가고 싶다
import sys
a,b,v = map(int,sys.stdin.readline().split())
speed = (v-b)/(a-b)
print(int(speed) if speed == int(speed) else int(speed) +1)

# 다른 방식!!!
import sys
a, b, v = map(int,sys.stdin.readline().split())
print((1-(v-a)//(a-b)))

