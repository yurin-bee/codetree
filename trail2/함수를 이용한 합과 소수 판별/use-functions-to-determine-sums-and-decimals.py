a, b = map(int, input().split())

def sosu(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def meow(n):
    nom = list(str(n))
    if sum(map(int, nom)) % 2 == 0:
        return True
    return False

cnt = 0
for i in range(a, b+1):
    if sosu(i) and meow(i):
        cnt += 1

print(cnt)