A = input()

# Please write your code here.

def alphabet(A):
    A = list(A)
    for i in range(len(A)):
        cnt = 0
        for j in A:
            if i == j:
                cnt += 1
        if cnt >= 2:
            return True
    return False
print(alphabet(A))