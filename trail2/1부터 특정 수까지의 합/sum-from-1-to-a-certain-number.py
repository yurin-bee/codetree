n = int(input())

# Please write your code here.

def hap(n):
    total = 0
    for i in range(1,n+1):
        total += i
    print(total//10)

hap(n)