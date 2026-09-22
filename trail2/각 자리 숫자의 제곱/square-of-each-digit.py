N = int(input())

# Please write your code here.

def func(N):
    if N % 10 == N:
        return N ** 2
    return func(N//10**2) + N%10**2
print(func(N))