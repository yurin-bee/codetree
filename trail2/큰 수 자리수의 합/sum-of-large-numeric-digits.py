a, b, c = map(int, input().split())

# Please write your code here.
n = a*b*c
def gob(n):
    if n % 10 == n:
        return n
    return n % 10 + gob(n//10)

print(gob(n))