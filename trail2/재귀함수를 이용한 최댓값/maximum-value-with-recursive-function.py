n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.

def find_max(i):
    if i == 0:
        return arr[0]
    return max(arr[i], find_max(i - 1))

print(find_max(n-1))