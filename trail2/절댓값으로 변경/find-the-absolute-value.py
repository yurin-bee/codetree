n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
def absf(n,arr):
    for i in range(n):
        arr[i] = abs(arr[i])

absf(n,arr)
print(*arr)