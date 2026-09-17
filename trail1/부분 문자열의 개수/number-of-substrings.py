a = input()
b = input()

la = len(a)
lb = len(b)

cnt = 0
for i in range(la-lb+1):
    if a[i:i+2] == b:
       cnt += 1
print(cnt) 