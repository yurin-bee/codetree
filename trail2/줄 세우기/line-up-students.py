n = int(input())
students = [tuple(map(int, input().split())) + (i + 1,) for i in range(n)]

students.sort(key=lambda x:(-x[0], -x[1], x[2]))

for stu in students:
    print(f"{stu[0]} {stu[1]} {stu[2]}")