string = list(input())
strr = []
for i in string:
    if ord(i) > 96:
        strr.append(chr(ord(i)-32))
    else:
        strr.append(chr(ord(i)+32))
print(''.join(strr))