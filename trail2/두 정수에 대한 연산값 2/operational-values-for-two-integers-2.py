a, b = map(int, input().split())

# Please write your code here.

def check(a, b):
    if a > b:
        b += 10
        a *= 2
        return a,b
    elif b > a :
        a += 10
        b *= 2
        return a,b
    
a,b = check(a,b)
print(a,b)
    