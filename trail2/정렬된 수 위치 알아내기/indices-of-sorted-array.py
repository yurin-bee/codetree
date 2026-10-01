n = int(input())
sequence = list(map(int, input().split())) 
#[3, 1, 6, 2, 7, 30, 1]

arr = []
for idx, num in enumerate(sequence, start=1):
    arr.append((idx,num))