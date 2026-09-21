n, m = map(int, input().split())

# Please write your code here.

def exchange(n,m):
    n,m=m,n
    return n,m
print(*exchange(n,m))