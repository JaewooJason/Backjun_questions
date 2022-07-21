# 8393 문제 합!

n = int(input())
sum = 0
if 1<= n <= 1000:
    for i in range(1,n+1):
        sum += i
print(sum)

# while 사용한 합 구하기

n = int(input())
sum = 0
i = 1
while i<=n:
    sum += i
    i += 1
print(sum)

# 15552 문제 빠른 A+B

import sys

T = int(input())

for i in range(T):
    a,b= map(int,sys.stdin.readline().rstrip())
    print(a+b)

t = int(sys.stdin.readline())

for i in range(t):
    a,b = map(int, sys.stdin.readline().split())
    print(a+b)

num = int(input())
total = []
for i in range(1,num+1):
    i.append(total)
# 단순하게 생각하면 풀릴때가 있다

num = int(input())

for i in range(1, num+1):
    print(i)

# 2742 문제 기찍 N

num = int(input())
for i in range(num,0,-1):
    print(i)

