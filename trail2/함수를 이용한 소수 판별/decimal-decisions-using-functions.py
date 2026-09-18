a, b = map(int, input().split())

# Please write your code here.

def sosu(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def meow(a,b):
    total = 0
    for i in range(a,b+1):
        if sosu(i) != False:
            total += i
    return total

print(meow(a,b))