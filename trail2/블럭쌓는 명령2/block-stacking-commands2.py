n, k = map(int, input().split())
commands = [tuple(map(int, input().split())) for _ in range(k)]

# Please write your code here.
diff = [0] * (n+2)
arr = [0] * (n+1)
for start, end in commands:
    diff[start] += 1
    diff[end+1] -= 1

cur = 0
for i in range(1, n+1):
    cur += diff[i]
    arr[i] = cur

print(max(arr))