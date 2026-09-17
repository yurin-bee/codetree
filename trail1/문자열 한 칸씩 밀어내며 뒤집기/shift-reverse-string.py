s, q = input().split()
q = int(q)
for _ in range(q):
    quest = int(input())
    if quest == 1:
        s = s[1:] + s[0]
    if quest == 2:
        s = s[-1] + s[0:-1]
    else:
        s = s[::-1]
    print(s)