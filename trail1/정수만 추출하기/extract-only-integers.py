a, b = input().split()

def output(string):
    for i in range(len(string)):
        if string[i].isdigit() == False:
            return int(string[:i])

result = output(a) + output(b)
print(result)