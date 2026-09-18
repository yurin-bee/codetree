def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a // b

operations = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': div,
}

a, op, b = input().split()
a, b = int(a), int(b)

if op in operations:
    result = operations[op](a, b)
    print(f"{a} {op} {b} = {result}")
else:
    print("False")