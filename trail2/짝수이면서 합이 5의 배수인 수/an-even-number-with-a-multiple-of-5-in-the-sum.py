n = int(input())
nm = str(n)

def nyan(n):
    if n % 2 == 0 and (int(nm[0]) + int(nm[1])) % 5 == 0:
        print("Yes")
    else:
        print("No")

nyan(n)