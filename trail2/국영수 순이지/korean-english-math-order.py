n = int(input())
name = []
korean = []
english = []
math = []

for _ in range(n):
    student_info = input().split()
    name.append(student_info[0])
    korean.append(int(student_info[1]))
    english.append(int(student_info[2]))
    math.append(int(student_info[3]))

# Please write your code here.\
class Student:
    def __init__(self, name, korean, english, math):
        self.n = name
        self.k = korean
        self.e = english
        self.m = math
 
arr = [Student(name[i], korean[i], english[i], math[i]) for i in range(n)]

arr.sort(key=lambda x:(-x.k, -x.e, -x.m), reverse=False)

for person in arr:
    print(f"{person.n} {person.k} {person.e} {person.m}")