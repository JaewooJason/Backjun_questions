#25304 영수증

x = int(input())
n = int(input())
price =()
for i in range(n):
    a, b = map(int, input().split())
    price.append(a,b)

# 위에 꺼는 처음에 시도 했던것

x = int(input())
n = int(input())
price =[]
for i in range(n):
    a, b = map(int, input().split())
    price_sum = a * b
    price.append(price_sum)
if x == sum(price):
    print('Yes')
else: print("No")
# 이게 정답

# 3003 체스

k = list(map(int, input().split()))
tmp_list = [1,1,2,2,2,8]
print(tmp_list-k)

#위에는 처음 시도

k = list(map(int, input().split()))
tmp_list = [1,1,2,2,2,8]
for i in range(6):
    print(tmp_list[i]-k[i], end=" ")

# 리스트 컴프레션을 사용한 경우
[print(b-int(a))for a,b in zip(input().split(),[1,1,2,2,2,8])]