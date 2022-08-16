# 10757 큰 수 A+B

import sys
a,b = map(int,sys.stdin.readline().split())
print(a+b)

# another way
print(sum(map(int,input().split())))

# 위에 두가지 방법으로 간단하게 할 수 있다.


# 1978 소수 찾기

n = int(input())
num = list(map(int,input().split(' ')))
cnt1 = 0

for nums in num:
    cnt2 = 0
    if nums == 1:
        continue
    for j in range(2, nums+1):
        if nums % j ==0:
            cnt2 +=1
    if cnt2==1:
        cnt1 +=1
print(cnt1)