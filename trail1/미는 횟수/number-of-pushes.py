A= input()
B= input()

yes = False
for i in range(1, len(A)+1):
    if A[-i:] + A[:-i] == B:
        yes = True
        break
    else:
        yes = False
        
if yes == True:
    print(i)
else:
    print(-1)