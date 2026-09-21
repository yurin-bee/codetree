n, m = map(int, input().split())
A = list(map(int, input().split()))

# Please write your code here.

def reduce(n, m, A):
    sum_value = 0
    while True:
        sum_value += A[m-1]
        if m % 2 == 1:
            m -= 1
        else:
            m //= 2
        if m == 1:
            sum_value += A[m-1]
            return sum_value

print(reduce(n,m,A))
    