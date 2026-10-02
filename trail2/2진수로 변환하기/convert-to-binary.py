n = int(input())

if n == 0:
    print(0)
else:
    arr = []
    while n >= 1:
        arr.append(n % 2)
        n //= 2
    for i in arr[::-1]:
        print(i, end="")