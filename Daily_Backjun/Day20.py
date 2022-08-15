# 2775 부녀회장이 될꺼야

t = int(input())

for i in range(t):
    f = int(input())
    n = int(input())
    b = [x for x in range(1, n+1)]
    for j in range(f):
        for k in range(1, n):
            b[k] += b[k-1]
    print(b[-1]) # 인덴트를 신경써야 한다.

# 2839 설탕배달

n = int(input())
bag = 0
while n >= 0 :
    if n %5 ==0: # 5의 배수이면
        bag += (n//5) # 5로 나눈 몫을 구해야 정수가 된다
        print(bag)
        break
    n -= 3
    bag +=1  # 5의 배수일때 설탕-3, 봉지+1
else:
    print(-1)