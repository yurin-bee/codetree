A = input()
B = input()

# Please write your code here.
la, lb = len(A), len(B)

while B in A:
    for i in range(la):
        if A.startswith(B, i):
            if i != 0:
                A = A[0:i] + A[i+lb:]
                break
            else:
                A = A[i+lb:]
                break
print(A)