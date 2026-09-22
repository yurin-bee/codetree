N = int(input())

def count(N):
    if N == 1:
        return 0
    if N % 2 == 0:
        return 1 + count(N // 2)
    else:
        return 1 + count(N // 3)

print(count(N))