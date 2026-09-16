n = int(input())
lst = [input() for _ in range(n)]
reference = input()

yes = []
for word in lst:
    if word[0] == reference:
        yes.append(len(word))

print(f"{len(yes)} {sum(yes)/len(yes):.2f}")

