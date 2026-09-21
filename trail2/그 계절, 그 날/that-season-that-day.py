y,m,d = map(int, input().split())

# Please write your code here.

def yoon(y):
    yoonn = True
    if y%4==0:
        if y % 100 == 0:
            yoonn = False
            if y % 400 == 0:
                yoonn = True
    else:
        yoonn = False
    return yoonn

def monthly(y,m,d):
        if m in [1,3,5,7,8,10,12] and 1<=d<=31:
            return True
        elif m in [4,6,9,11] and 1<=d<=30:
            return True
        elif m == 2:
            if yoon(y) and 1<=d<=29:
                return True
            elif yoon(y) == False and 1<=d<=28:
                return True
        else:
            return False 

def weather(y,m,d):
    if monthly(y,m,d):
        if 3<=m<=5:
            print("Spring")
        elif 6<=m<=8:
            print("Summer")
        elif 9<=m<=11:
            print("Fall")
        elif m in [12,1,2]:
            print("Winter")
        else:
            print(-1)
    else:
        print(-1)

weather(y,m,d)