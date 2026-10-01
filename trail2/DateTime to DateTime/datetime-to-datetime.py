a, b, c = map(int, input().split())

# Please write your code here.

start = (11 - 1) * 24 * 60 + 11 * 60 + 11
end = (a - 1) * 24 * 60 + b * 60 + c

diff = end - start
print(diff if diff >= 0 else -1)