N = int(input())

# Please write your code here.

def func(N):
    if N % 10 == N:
        return N ** 2
    return (N % 10) ** 2 + func(N//10)
print(func(N))