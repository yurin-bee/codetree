A= input()
B= input()

cnt = 0
for i in range(1, len(A)+1):
    cnt += 1
    if A[i:] + A[:i] == B:
        break
print(cnt)