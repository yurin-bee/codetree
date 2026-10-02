n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

OFFSET = 100          # -100 ~ 100 좌표를 0 ~ 200으로 밀어주기 위한 값
diff = [0] * 202       # 0~201칸 (여유 포함)

for x1, x2 in segments:
    diff[x1 + OFFSET] += 1
    diff[x2 + OFFSET] -= 1

cur = 0
max_overlap = 0
for i in range(202):
    cur += diff[i]
    max_overlap = max(max_overlap, cur)

print(max_overlap)