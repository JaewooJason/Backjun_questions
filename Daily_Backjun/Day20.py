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