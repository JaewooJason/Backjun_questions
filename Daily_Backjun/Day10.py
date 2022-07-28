# 10818 문제 최소, 최대

n = int(input())
array = list(map(int,input().split()))

for i in array:
    print(max(i))
    print(min(i))

n = int(input())
array = list(map(int,input().split()))

print(max(array))
print(min(array))

# 2562 문제 최댓값

list = []

for i in range(9):
    list.append(map(int,input().split()))

print(max(list))
print(list.index(max(list)))
# 위에껀 처음에 잘못만든 코드
list = []

for i in range(9):
    list.append(int(input()))

print(max(list))
print(list.index(max(list))+1)

# 2577 문제 숫자의 개수
a = int(input())
b = int(input())
c = int(input())
abc = a*b*c
# 여기서 중요한것은 결과값을 어떻게 가지고 올것인가 이다. 카운트함수는 문자열에서만 가능하기 때문에 변환도 무조건 생각해야한다.
for i in range(10):
    print(abc.count(str(abc[i])))

# 밑이 정답 중요한점은 리스트로 담는것이다. 리스트로 담을때는 정수형이 아닌 문자형으로 변환하여 하나하나가 리스트안에 요소가 되도록 해야한다.
a = int(input())
b = int(input())
c = int(input())
abc = list(str(a*b*c))

for i in range(10):
    print(abc.count(str(i)))

