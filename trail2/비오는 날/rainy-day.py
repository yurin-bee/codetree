n = int(input())
date = []
day = []
weather = []

for _ in range(n):
    d, dy, w = input().split()
    date.append(d)
    day.append(dy)
    weather.append(w)

# Please write your code here.

class Days:
    def __init__(self, date, day, weather):
        self.d = date
        self.day = day
        self.w = weather

arr = [Days(date[i], day[i], weather[i]) for i in range(n)]
early = None
for ar in arr:
    if ar.w == "Rain":
        if early is None or early.d > ar.d:
            early = ar
print(f"{early.d} {early.day} {early.w}")
