n = int(input())
name = []
height = []
weight = []

for _ in range(n):
    n_i, h_i, w_i = input().split()
    name.append(n_i)
    height.append(int(h_i))
    weight.append(int(w_i))

# Please write your code here.
class People:
    def __init__(self, name, height, weight):
        self.n = name
        self.h = height
        self.w = weight
    
arr = [People(name[i], height[i], weight[i]) for i in range(n)]

arr.sort(key=lambda x:x.h)
for ar in arr:
    print(f"{ar.n} {ar.h} {ar.w}")