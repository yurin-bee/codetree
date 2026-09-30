n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
for i in range(n):
    if i % 2 == 0:
        meow = sorted(arr[0:i+1])
        print(meow[i//2], end=" ")