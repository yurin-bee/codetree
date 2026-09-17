n = input()
total = 0

for _ in range(int(n)):
    total += int(input())

total = str(total)
result = total[1:] + total[0]
print(result)