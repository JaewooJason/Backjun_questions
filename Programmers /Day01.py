''' 첫번째 문제 - 문자열 s의 길이가 4 혹은 6이고, 숫자로만 구성돼있는지 확인해주는 함수,
 solution을 완성하세요. 예를 들어 s가 "a234"이면 False를 리턴하고 "1234"라면 True를 리턴하면 됩니다.'''

def solution(s):
    if (len(s)== 4 or len(s) == 6)&(s.isdigit()):
        answer = True
    else:
        answer = False
    return answer
# 위의 문제에서는 isdigit이라는것이 중요했다. 문제를 자주보고 이해하는것이 먼저인거 같다.

''' 비밀지도 '''

def solution(n,arr1,arr2):
    answer = []
    for i in range(n):
        tmp = bin(arr1[i] | arr2[i])
        tmp = tmp[2:].zfill(n)
        tmp = tmp.replace("1",'#').replace('0',' ')
        answer.append(tmp)
    return answer
# 여기서는 비트연산자를 어떻게 사용할지에 대해서 중요하다. 그리고 문제에서 2진법으로 하라는 힌트를 주었을때 2진법으로 바꾸어주는 bin메서드를 사용하는것을 떠올려야하는데 떠오르지 않았다. 공부를 더해야겠다.