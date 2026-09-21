n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.

def check(n, arr):
    for i in range(n):
        if arr[i] % 2 == 0:
            arr[i] //= 2

check(n,arr)
print(*arr)