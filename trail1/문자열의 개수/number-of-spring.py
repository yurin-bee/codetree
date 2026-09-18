lst = []

while True:
    s = input()
    if s.isdigit() != False:
        break
    else:
        lst.append(s)

print(len(lst))
for i in lst[::2]:
    print(i)