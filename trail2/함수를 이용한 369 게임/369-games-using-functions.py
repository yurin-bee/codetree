a, b = map(int, input().split())

def function(a, b):
    cnt = 0
    for i in range(a, b+1):
        s = str(i)
        if '3' in s or '6' in s or '9' in s:
            if i % 3 == 0:
                cnt += 1
    return cnt

print(function(a, b))