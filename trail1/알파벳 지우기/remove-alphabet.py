a = input()
b = input()

def num(string):
    number = []
    for i in string:
        if i.isdigit():
            number.append(i)
    result = ''.join(number)
    return int(result)

print(num(a)+num(b))