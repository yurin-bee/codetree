n = int(input())
loc = 0
color = {}

for _ in range(n):
    x, d = input().split()
    x = int(x)
    if d == 'L':
        for p in range(loc - x + 1, loc + 1):
            color[p] = 'W'
        loc -= x - 1
    else:
        for p in range(loc, loc + x):
            color[p] = 'B'
        loc += x - 1
vals = list(color.values())
print(vals.count('W'), vals.count('B'))