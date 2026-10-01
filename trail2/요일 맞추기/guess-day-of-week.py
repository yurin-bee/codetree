m1, d1, m2, d2 = map(int, input().split())

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

doy1 = sum(months[1:m1]) + d1
doy2 = sum(months[1:m2]) + d2

print(days[(doy2 - doy1) % 7])