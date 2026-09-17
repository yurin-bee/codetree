word = input()

new = word[0:1] + 'a' + word[2:-2] + 'a' + word[-1]
print(new)