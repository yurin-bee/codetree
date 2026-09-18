n, m = map(int, input().split())

# Please write your code here.

def square(n,m):
    arr = [[1 for i in range(m)] for j in range(n)]
    for row in arr:
        print(''.join(map(str,row)))
square(n,m)