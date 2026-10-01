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

arr = [(name[i], height[i], weight[i]) for i in range(n)]
arr.sort(key=lambda x:(x[1],-x[2]))
for ar in arr:
    print(f"{ar[0]} {ar[1]} {ar[2]}")