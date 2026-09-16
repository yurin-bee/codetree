A = input()

result = []
cur = A[0]
cnt = 1

for i in A[1:]:
    if i == cur:
        cnt += 1
    else:
        result.append(cur)
        result.append(cnt)
        cur = i
        cnt = 1

result.append(cur)
result.append(cnt)

encoded = ''.join(str(x) for x in result)
print(len(encoded))
print(encoded)