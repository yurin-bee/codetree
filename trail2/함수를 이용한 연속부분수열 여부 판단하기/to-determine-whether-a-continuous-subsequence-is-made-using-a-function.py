n1, n2 = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# Please write your code here.

def comparison(a,b):
    for i in range(len(a)-len(b)+1):
        if a[i:len(b)+i] == b:
            return True
    return False 

if comparison(a,b):
    print("Yes")
else:
    print("No")