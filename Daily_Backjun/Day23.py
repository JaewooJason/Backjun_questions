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

