# 1065 문제 한수

def hansu(n):
    cnt = 0
    for i in range(1,n+1):
        tmp_list = list(map(int,str(i)))
        if i <100:
            cnt +=1
        elif tmp_list[0]-tmp_list[1] == tmp_list[1]-tmp_list[2]:
            cnt +=1
    return cnt
num = int(input())
print(hansu(num))