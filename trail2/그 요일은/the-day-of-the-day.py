m1, d1, m2, d2 = map(int, input().split())
A = input()

# Please write your code here.

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
months = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

start_day = sum(months[:m1]) + d1
end_day = sum(months[:m2]) + d2
result = end_day - start_day
count = result // 7
count1 = result % 7
if A in days[:count1+1]:
    count += 1
print(count)