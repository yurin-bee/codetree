n, m = map(int, input().split())
arr = list(map(int, input().split()))
queries = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.


def hap(queries, arr):
    for q1, q2 in queries:
        print(sum(arr[q1-1:q2]))

hap(queries, arr)