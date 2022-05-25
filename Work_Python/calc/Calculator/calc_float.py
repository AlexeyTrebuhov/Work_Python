def calc(a: float, b: float, operation: str):
    a = float(a)
    b = float(b)
    if operation == '+':
        return a+b
    if operation == '-':
        return a-b
    if operation == '*':
        return a*b
    if operation == '/':
        return a/b
