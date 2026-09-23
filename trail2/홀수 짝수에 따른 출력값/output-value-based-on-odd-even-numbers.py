N = int(input())

# Please write your code here.

def check(N):
    if N == 1:
        return 1
    if N == 2:
        return 2
    return N + check(N-2)

print(check(N))