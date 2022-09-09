# 10872 팩토리얼

def num(n):
    result = 1
    if n > 0:
        result = n * num(n - 1)
    return result


n = int(input())
print(num(n))

# 다른 방법

def fac(n):
    if n == 0:
        return 1
    return num * fac(n-1)
n = int(input())
print(fac(n))