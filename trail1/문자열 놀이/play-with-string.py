s, q = input().split()
q= int(q)

for i in range(q):
    a, b, c = input().split()
    a = int(a)

    if a == 1:
        s = list(s)
        b = int(b) - 1
        c = int(c) - 1
        temp = s[b]
        s[b] = s[c]
        s[c] = temp
        s = ''.join(s)
    if a == 2:
        s= s.replace(b, c)
    print(s)