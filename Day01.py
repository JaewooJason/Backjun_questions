# 고양이 만들기
print('\\    /\\')
print(" )  ( ')")
print('(  /  )')
print(' \\(__)|')
# 강아지 만들기
print('*'*30)
print('|\\_/|')
print('|q p|   /}')
print('( 0 )"""\\')
print('|"^"`    |')
print('||_/=\\\\__|')
# A+B
a,b = map(int, input().split())
print(a+b)

# A-B
a,b = map(int,input().split())
print(a-b)

# A*B
a,b = map(int,input().split())
print(a*b)

# A/B
a,b = map(int,input().split())
print(a/b)

# 사칙연산
def f(a,b):
    print(a+b)
    print(a-b)
    print(a*b)
    print(a/b)
    print(a%b)
a,b = map(f,input().split())
''' 위에 했던것이 처음에 할려고 시도 했던것 '''
a,b = map(int,input().split())
print(a+b)
print(a-b)
print(a*b)
print(int(a/b))
print(a%b)

# 다른 방법으로는
a,b = input().split()
a= int(a)
b= int(b)
print(f'{a+b}\n{a-b}\n{a*b}\n{a/b}\n{a%b}')

# 백준 10925문제 아주 간단했는데 쉽게 풀지 못함..... 노력이 필요하다고 느낀다.

id = input()
print(id +'??!')




