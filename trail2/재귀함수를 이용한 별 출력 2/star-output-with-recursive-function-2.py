n = int(input())

# Please write your code here.

def star(n):
    if n == 0:
        return
    print(("* " * n).rstrip())
    star(n-1)
    print(("* " * n).rstrip())

star(n)