# 4948 베르트랑 공준
def so(n):
    if n == 1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i == 0:
            return False
    return True
range_list = list(range(2, 246912))
sosu =[]

for i in range_list:
    if so(i):
        sosu.append(i)

n = int(input())

while True:
    cnt = 0
    if n ==0:
            break
    for i in sosu:
        if n<i<=2*n:
            cnt+=1
    print(cnt)
    n = int(input())

# 9020 골드바흐의 추축

def gold(n):
    if n ==1:
        return False
    for i in range(2,int(n**0,5)+1):
        if n % i ==0:
            return False
    return True
for _ in range(int(input())):
    num = int(input())
    a,b = num//2, num//2
    while a>0:
        if gold(a) and gold(b):
            print(a,b)
        else:
            a -= 1
            b += 1

import sys

tmp_list= [False,False] +[True]*10002

for i in range(2, 10002):
    if tmp_list[i]:
        for j in range(2*i, 10002, i):
            tmp_list[j]= False
t = int(sys.stdin.readline())

for y in range(t):
    n = int(sys.stdin.readline())
    a = n//2
    b = a
    while a > 0 :
        if tmp_list[a] and tmp_list[b]:
            print(a,b)
            break
        else:
            a-=1
            b+=1

