n = int(input())

# Please write your code here.
def function(n):
    if n == 0:
        return
    print(n, end=" ")
    function(n-1)
    print(n, end=" ")

function(n)

