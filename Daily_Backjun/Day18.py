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

