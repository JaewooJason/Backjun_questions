# 2775 부녀회장이 될꺼야

t = int(input())

for i in range(t):
    floor = int(input())
    num = int(input())
    base = [x for x in range(1, num+1)]
    for j in range(floor):
        for k in range(1, num):
            base[k] += base[k-1]
        print(base[-1])