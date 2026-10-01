m1, d1, m2, d2 = map(int, input().split())

# Please write your code here.

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if m1 == m2:
    print(days[(d2 - d1) % 7])
else:
    print(days[(sum(months[m1+1:m2]) + (d2-d1)) % 7])