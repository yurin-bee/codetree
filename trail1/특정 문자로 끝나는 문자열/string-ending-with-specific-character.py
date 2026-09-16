lst = []
for i in range(10):
    word = input()
    lst.append(word)
n = input()

hey = False
for w in lst:
    if w[-1] == n:
        print(w)
        hey = True
if hey == False:
    print("None")
