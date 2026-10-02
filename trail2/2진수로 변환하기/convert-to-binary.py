n = int(input())

# Please write your code here.

arr = []
while True:
    if n < 2:
        arr.append(1)
        break
    arr.append(n%2)
    n //= 2 

for i in arr[::-1]:
    print(i, end="")