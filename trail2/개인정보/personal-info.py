N = 5
name = []
height = []
weight = []

for _ in range(N):
    n, h, w = input().split()
    name.append(n)
    height.append(int(h))
    weight.append(float(w))

# Please write your code here.

arr = [(name[i], height[i], weight[i]) for i in range(N)]
arr.sort(key=lambda x:x[0])
print("name")
for ar in arr:
    print(f"{ar[0]} {ar[1]} {ar[2]}")
arr.sort(key=lambda x:-x[1])
print()
print("height")
for ar in arr:
    print(f"{ar[0]} {ar[1]} {ar[2]}")