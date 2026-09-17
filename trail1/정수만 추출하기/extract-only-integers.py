a, b = input().split()

def output(string):
    for i in range(len(string)):
        if not string[i].isdigit():
            return int(string[:i])
    return int(string)

result = output(a) + output(b)
print(result)