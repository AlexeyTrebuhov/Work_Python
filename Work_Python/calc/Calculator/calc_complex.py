def calc(a: complex, b: complex, operation: str):
    a = complex(a)
    b = complex(b)
    if operation == '+':
        return a+b
    if operation == '-':
        return a-b
    if operation == '*':
        return a*b
    if operation == '/':
        return a/b
