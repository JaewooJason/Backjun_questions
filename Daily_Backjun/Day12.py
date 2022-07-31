# 8985 문제 OX
t = int(input())
for i in range(t):
    b = input()
    c = list(b)
    sum = 0
    cnt = 1
    for i in c:
        if i == "O":
            sum += cnt
            cnt += 1
        else:
            cnt = 1
    print(sum)
''' 이 문제는 수열을 잘 이해해야한다. 처음에 어떻게 해야할지 몰랐던 부분은 어떻게 증가하는 것을 추가하는것이였고, for 구문이 두개가
 들어가는것이였다. 이러한 문제는 많이 보고 어떤식으로 문제를 풀어야할지에 대하여 눈으로 익혀야 할거 같다. '''

# 4344 문제 평균은 넘겠지?

t = int(input())
for i in range(t):
    tmp_list = list(map(int,input().split()))
    avg = sum(tmp_list[1:])/tmp_list[0]
    cnt =0
    for score in tmp_list[1:]:
        if score > avg:
            cnt += 1
    rate = cnt/tmp_list[0]*100
    print(f'{rate:.3f}%')

# 이 문제 역시 for 구문의 대한 사용에 대한 이해가 필요하다.

def solve(a):
    return sum(a)

# 4673 문제 셀프넘버 이건 너무 어렵다..... 이해가 많이 필요,,,,,,
def d(n):
    n = n + sum(map(int, str(n)))
    return n


nonself = set()

for i in range(1, 10001):
    nonself.add(d(i))

for j in range(1, 10001):
    if j not in nonself:
        print(j)