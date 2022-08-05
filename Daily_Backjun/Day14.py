# 11720 숫자의 합
# for 구문 사용해서 만든 답

t = int(input())
n = input()
total = 0
for i in n:
    total += int(i)
print(total)

# for 구문 사용하지 않고 만든 답

t = int(input())
print(sum(map(int,input())))

# 10809 문제 알파벳 찾기

word = input()
alp = list(range(97,123))# 아스키 코드에 대한 이해가 필요 그냥 아스키 코드 외우기
for i in alp:
    print(word.find(chr(i)))

# 2675 문제 문자열 반복

t = int(input())

for _ in range(t):
    s, word = input().split()
    for i in word:
        print(i*int(s), end='')
    print()

# 1157 단어장

word = input().lower()
tmp_list = list(set(word))
cnt = []

for i in tmp_list:
    count = word.count(i)
    cnt.append(count)
if cnt.count(max(cnt))>2:
    print('?')
else: print(tmp_list[(cnt.index(max(cnt)))].upper())

