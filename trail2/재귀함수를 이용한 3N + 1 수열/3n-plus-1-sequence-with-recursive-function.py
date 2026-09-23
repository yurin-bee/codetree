n = int(input())

# Please write your code here.
cnt=0
def func(n):
    global cnt
    if n == 1:
        return
    if n % 2 == 0:
        cnt += 1
        n //= 2
    else:
        n = n * 3 + 1
        cnt += 1
    func(n)
     

func(n)
print(cnt)
