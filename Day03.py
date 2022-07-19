# 25083 새싹만들기
print('         ,r\'\"7')
print('r`-_   ,\'  ,/')
print(' \. \". L_r\' ')
print('   `~\/')
print('      |')
print('      |')
print("한방에 성공!!!!")
'''
         ,r'"7
r`-_   ,'  ,/
 \. ". L_r'
   `~\/
      |
      |
'''

# 2단계 시작!!!
# 1330문제 두수 비교하기

num1, num2 = map(int,input().split())

if -10000<= num1 & 10000 >= num2:
    if num1 < num2 :
        print('<')
    elif num1 > num2:
        print('>')
    else:
        print('==')

if -10000 <= num1 >= 10000 and -10000 <= num2 >= 10000:
    if num1 < num2 :
        print('<')
    elif num1 > num2:
        print('>')
    else:
        print('==')

num1, num2 = map(int,input().split())

if -10000 <= num1 <= 10000 and -10000 <= num2 <= 10000:
    if num1 > num2 :
        print('>')
    elif num1 < num2:
        print('<')
    else: print('==')


# 9498 문제 시험 성적

score = int(input())
if 0<= score <= 100:
    if 90<= score <=100:
        print('A')
    elif 80<= score <=89:
        print('B')
    elif 70<= score <= 79:
        print('C')
    elif 60<= score <=69:
        print('D')
    else: print('F')

# 2753 문제 윤년

year = int(input())

if (year%4==0 & year%100 != 0) or (year%400==0):
    print('1')
else:print('0')


# 14681 사분면 문제
import sys

x = int(sys.stdin.readline())
y = int(sys.stdin.readline())

if (-1000<= x <= 1000 & x!=0 ) and (-1000 <= y <= 1000 & y != 0):
    if (1 <= x <= 1000) and (1<= y <= 1000):
        print('1')
    elif (-1000 <= x <= -1) and (1 <= y <= 1000):
        print('2')
    elif (1 <= x <= 1000) and (-1000<= y <= -1):
        print('4')
    else: print('3')

x, y = map(int, input().split())

if 0>x & 0>y:
    print('1')
elif 0<x & 0>y:
    print('2')
elif 0<x & 0<y:
    print('3')
else: print('4')

x, y = map(int,input().split())
if x>0:
    if y>0:
        print('1')
    else:
        print('4')
else:
    if y>0:
        print('2')
    else:
        print('3')

# finally I solved this question......
x= int(input())
y= int(input())
if x>0:
    if y>0:
        print('1')
    else:
        print('4')
else:
    if y>0:
        print('2')
    else:
        print('3')

