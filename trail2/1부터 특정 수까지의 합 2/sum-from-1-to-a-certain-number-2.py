N = int(input())

# Please write your code here.

def add(N):
    if N == 1:
        return 1
    return N + add(N-1) 

print(add(N))