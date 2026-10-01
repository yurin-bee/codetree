m1, d1, m2, d2 = map(int, input().split())

# Please write your code here.
calendar = [0,31,28,31,30,31,30,31,31,30,31,30,31]
end_day = sum(calendar[0:m2]) + d2
start_day = sum(calendar[0:m1]) + d1
print(end_day - start_day + 1)