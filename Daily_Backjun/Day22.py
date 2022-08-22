# 11653 소인수분해

n = int(input())
if n ==1 :
    print('')
for i in range(2,n+1):
    if n % i == 0:
        while n % i == 0:
            print(i)
            n = n/i
# 아직 너무 어렵다...... 제발 하루하루 늘어가기를

# 1929 소수찾기

m,n = map(int,input().split())

for i in range(m, n+1):
    if i ==1:
        continue
    for j in range(2,int(i**0.5)+1):
        if i %j ==0:
            break
    else:
        print(i)