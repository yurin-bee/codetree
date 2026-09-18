n, m = map(int, input().split())

# Please write your code here.
def choi(n, m):
    for i in range(1, 101):
        if i % n == 0 and i % m ==0:
            print(i)
            break

choi(n,m)

