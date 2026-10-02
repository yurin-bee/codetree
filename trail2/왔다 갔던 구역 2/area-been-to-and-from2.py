n = int(input())
OFFSET = 1000
diff = [0] * (2 * OFFSET + 2)

cur = 0
for _ in range(n):
    x, d = input().split()
    x = int(x)
    nxt = cur - x if d == 'L' else cur + x

    lo, hi = min(cur, nxt), max(cur, nxt)
    diff[lo + OFFSET] += 1
    diff[hi + OFFSET] -= 1

    cur = nxt

count = 0
cursum = 0
for v in diff:
    cursum += v
    if cursum >= 2:
        count += 1

print(count)