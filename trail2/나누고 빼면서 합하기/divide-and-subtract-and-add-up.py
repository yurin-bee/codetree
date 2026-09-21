n, m = map(int, input().split())
A = list(map(int, input().split()))

# Please write your code here.

def reduce(n,m,A):
    sum = 0
    while True:
        sum += A[m-1]
        if m == 1:
            return sum
        if m % 2 == 1:
            m -= 1
        else:
            m //= 2


print(reduce(n,m,A))
    