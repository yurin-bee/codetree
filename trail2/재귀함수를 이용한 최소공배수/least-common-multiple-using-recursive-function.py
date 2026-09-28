n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def lcm(a, b):
    return a * b // gcd(a, b)

def find_lcm(i):
    if i == 0:
        return arr[0]
    return lcm(arr[i], find_lcm(i - 1))

print(find_lcm(n - 1))