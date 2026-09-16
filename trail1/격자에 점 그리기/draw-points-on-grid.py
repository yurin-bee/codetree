n, m = map(int, input().split())

sqr = [[0 for _ in range(n)] for _ in range(n)]

cnt = 1

for i in range(m):
    a, b = map(int, input().split())
    sqr[a-1][b-1] = cnt 
    cnt += 1

for row in sqr:
    print(' '.join(map(str, row)))