# 1712 문제 손익분기점

a, b, c = map(int,input().split())
if b >= c:
    print('-1')
else:
    print(a//(c-b)+1)

# 2292 문제 벌집

n = int(input())
bee = 1
cnt = 1
while n > bee:
    bee += 6 *cnt
    cnt += 1
print(cnt)


# 1193 분 찾기

import sys
input = sys.stdin.readline
n = int(input())
f_line = 1
while n > f_line:
    n -= f_line
    f_line += 1

if f_line % 2 == 0:
    num1 = n
    num2 = f_line - n + 1
elif f_line % 2 == 1:
    num1 = f_line - n + 1
    num2 = n
print(num1, '/', num2, sep="")