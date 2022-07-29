# 1546 문제 평균

n = int(input())
score = list(map(int,input().split()))
max_score = max(score)

new_list =[]

for i in score:
    new_list.append(i/max_score*100)
new_avg = sum(new_list)/n

print(new_avg)