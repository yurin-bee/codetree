n, k, t = input().split()
n, k = int(n), int(k)
str = [input() for _ in range(n)]

# Please write your code here.
dictionary = []
for string in str:
    if string[0:len(t)] == t:
        dictionary.append(string)
dictionary.sort()
print(dictionary[k-1])