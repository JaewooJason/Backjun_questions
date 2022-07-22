# 11021 문제 A+B -7
t = int(input())
cnt = 0
for i in range(t):
    cnt+=1
    a,b= map(int, input().split())
    print(f'Case #%d: %d' % (cnt, a+b))

# 11022 문제 A+B -8

t = int(input())
cnt=0
for i in range(t):
    cnt+= 1
    a,b = map(int,input().split())
    print(f'Case #%d: %d + %d = %d' % (cnt, a, b, a+b))

# 2438 문제 별찍기 -1

star = int(input())

for i in range(star):
    print('*'* i)
    # 좀 더 생각하고 문제를 풀자!!! 정답이 아니다

star = int(input())
for i in range(1, star+1):
    print('*'*i)
