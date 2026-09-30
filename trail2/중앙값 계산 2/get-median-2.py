n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
order = 1
for i in range(n):
    if i == 0:
        print(arr[0])
    elif i % 2 == 0:
        print(sorted(arr[:i+1]).std())