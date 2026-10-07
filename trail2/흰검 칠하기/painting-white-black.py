N = int(input())
loc = 0
cnt = {}    # 타일 -> [흰색 칠한 횟수, 검은색 칠한 횟수]
last = {}   # 타일 -> 마지막으로 칠한 색 (0=흰, 1=검)

for _ in range(N):
    x, d = input().split()
    x = int(x)
    if d == 'L':
        tiles, c = range(loc, loc - x, -1), 0     # loc, loc-1, ..., loc-x+1
        loc -= x - 1
    else:
        tiles, c = range(loc, loc + x), 1         # loc, ..., loc+x-1
        loc += x - 1

    for p in tiles:
        cnt.setdefault(p, [0, 0])[c] += 1
        last[p] = c

gray = sum(1 for w, b in cnt.values() if w >= 2 and b >= 2)
black = sum(1 for p, (w, b) in cnt.items() if not (w >= 2 and b >= 2) and last[p] == 1)
white = len(cnt) - gray - black

print(white, black, gray)