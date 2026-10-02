n = int(input())
loc = 0
offset = 100_000
diff = [0] * ((offset*2) + 2)
segment = []
for _ in range(n):
    x, dir = input().split()
    x = int(x)
    if dir == 'R':
        segment.append((loc, loc+x))
        loc += x
    else:
        segment.append((loc-x, loc))
        loc -= x
print(segment)