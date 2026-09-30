MAX_N = 5

users = []
for _ in range(MAX_N):
    codename, score = input().split()
    users.append((codename, int(score)))

# Please write your code here.
min_user = users[0]
for user in users:
    if user[1] < min_user[1]:
        min_user = user

print(min_user[0], min_user[1])