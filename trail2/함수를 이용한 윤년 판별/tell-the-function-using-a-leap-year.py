y = int(input())

# Please write your code here.

def yoon(y):
    if y % 4 == 0:
        if y % 100 == 0 and y % 400 != 0:
            return False
            break
        return True
    return False

if yoon(y):
    print("true")
else:
    print("false")