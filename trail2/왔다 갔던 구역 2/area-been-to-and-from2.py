n= int(input())
offset = 1000
diff = [0] * ((2* offset) + 2) 
segment = []
loc = 0
for i in range(n):
    x, dir = input().split()
    x = int(x)
    if dir == "R":
        segment.append((loc, loc+x))
        loc += x
    else:
        segment.append((loc-x, loc))
        loc -= x

for start, end in segment:
    diff[start + offset] += 1
    diff[end + offset] -= 1

for i in range(1, len(diff)):
    diff[i] += diff[i-1]

print(sum(1 for v in diff if v >= 2))

