m,d = map(int, input().split())

# Please write your code here.

def existence(m,d):
    if m == 2 and (1<=d<=28):
        return True
    elif m in [1,3,5,7,8,10,12] and (1<=d<=31):
        return True
    elif m in [4,6,9,11] and (1<=d<=30):
        return True
    else:
        return False

if existence(m,d):
    print("Yes")
else:
    print("No")