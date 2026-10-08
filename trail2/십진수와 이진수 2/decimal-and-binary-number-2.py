N = input()
array = []
for n in N:
    array.append(int(n))
# Please write your code here.
num = 0

for i in range(len(array)):
    num = num * 2 + array[i]

num *= 17
digitss = []
while True:
    if num < 2:
        digitss.append(num)
        break
    else:
        digitss.append(num%2)
        num //= 2
for j in digitss[::-1]:
    print(j,end="")