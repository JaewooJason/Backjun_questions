# 10872 팩토리얼

def num(n):
    result = 1
    if n > 0:
        result = n * num(n - 1)
    return result


n = int(input())
print(num(n))
