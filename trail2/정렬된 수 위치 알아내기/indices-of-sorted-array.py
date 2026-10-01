n = int(input())
sequence = list(map(int, input().split())) 
#[3, 1, 6, 2, 7, 30, 1]

arr = []
for idx, num in enumerate(sequence, start=1):
    arr.append((idx,num))
arr.sort(key=lambda x:(x[1],x[0]))
order = [0] * (n+1)

for rank,(idx,num) in enumerate(arr,start=1):
    order[idx] = rank
print(*order[1:n+1])
