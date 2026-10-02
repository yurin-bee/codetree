n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
diff = [0] * 102
arr = [0] * 101

for s, e in segments:
    diff[s] += 1
    diff[e+1] -= 1

max_value = 0
cur = 0
for i in range(1, 101):
    cur += diff[i]
    max_value = max(max_value, cur)
print(max_value)