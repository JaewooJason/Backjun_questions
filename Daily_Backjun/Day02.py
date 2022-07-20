# 18108 문제
year = int(input().split())
print(year-543)
# 처음에는 이렇게 했는데 런타임 에러
year = int(input().split())
print(year-543)
# 여기서 중요한것은 input으로 들어온 값을 int값으로 변경하는것이 중요하다고 판단됩니다.

# 10430 문제

A = int(input())
B = int(input())
C = int(input())
print((A+B)%C)
print((A%C)+(B%C)%C)
print((A*B)%C)
print((A%C)*(B%C)%C)

A,B,C = map(int,input().split())
print((A+B)%C)
print(((A%C)+(B%C))%C)
print((A*B)%C)
print(((A%C)*(B%C))%C)

# 2588 문제
a = int(input())
b = int(input())

for i in range(len(b),0,-1):
    print(a * int(b[i-1]))

print(a*b)

print('n번째 시도...')
num1 = int(input())
num2 = int(input())

print(num1 * (num2%10))
print(num1 * ((num2%100)//10))
print(num1 * (num2 // 100))
print(num1 * num2)
