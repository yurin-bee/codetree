n = int(input())

# Please write your code here.

#from 1 to n
def one(n):
    if n == 0:
        return
    one(n-1)
    print(n, end=" ")

#from n to 1
def nnn(n):
    if n == 0:
        return
    print(n, end=" ")
    nnn(n-1)

one(n)
print()
nnn(n)