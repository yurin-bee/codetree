def reduce(n, m, A):
    sum_value = 0
    while True:
        sum_value += A[m-1]
        if m == 1:              # ← 값 더하고 나서, m을 아직 안 건드린 상태에서 바로 체크
            return sum_value
        if m % 2 == 1:
            m -= 1
        else:
            m //= 2