# 2884 문제 알람시계
''' 이 문제에서 중요한것은 45분이상일때는 시간의 변화는 없고 45분 이하일때는 시간의 변화가 발생한다 그리고 0시이면 23로 변환해야하는 것을 유의해야한다.'''

H,M = map(int(input()))

if 0<= H <= 23 and 0 <= M <= 59:
    if M >= 45:
        M -= 45
        print(H,M)
    else:
        M = M + 60 - 45
        if H ==0:
            H = 23
        else:
            H -= 1
        print(H, M)
# 다른 형태로 풀어보기
h,m = map(int,input().split())

if m >= 45:
    print(h, m- 45)
elif h >0 and m < 45:
    print(h-1, m+ 15)
else:
    print(23, m+ 15)

hour, min = map(int,input().split())

if min<=45:
    if hour == 0:
        hour = 23
        min += 60
    else:
        hour -= 1
        min += 60

# 2525 문제 오븐시간

h,m = map(int,input().split())
o = int(input())
h += o// 60
m += o% 60

if m >= 60:
    h+= 1
    m-=60
if h >=24:
    h -= 24
print('%d %d' % (h,m))

a,b,c = map(int,input().split())

if a == b == c:
    print(10000+a*1000)
elif a == b:
    print(1000 + a*100)
elif a ==c:
    print(1000 + a * 100)
elif b == c:
    print(1000 + b *100)
else:
    print(100* max(a,b,c))

# 2739 문제 구구단
n = int(input())

if 1<= n <=9:
    for i in n:
        print(i* range(1,9))


n = int(input())

if 1<= n <=9:
    for i in range(1,10):
        print('%d * %d = %d' % (n,i,(n*i)))

# 10950 문제 A+B -3

t = int(input())

for i in range(t):
    a,b = map(int,input().split())
    print(a+b)









