# 1110 문제
n = int(input())
num = n
cnt = 0

while 1:
    a = num // 10
    b = num %10
    c = (a + b) % 10
    num = (b*10)+c
    cnt += 1
    if (n == num):
        break
print(cnt)
# 기본적으로 하나하나 뜯어서 어떻게 10의 자리 1의 자리를 연결할지에 대해서 고민해봐야 하는 문제이다.
''' 문자열로 해서 문제를 풀 경우'''

n = input()
num = n
cnt =0

while 1:
    if len(num)==1:
        '0' + num
    plus = str(int(num[0])+int(num[1]))
    num = num[-1] + plus[-1]
    cnt +=1
    if n == num:
        print(cnt)
        break

