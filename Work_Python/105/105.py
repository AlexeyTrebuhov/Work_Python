# для текущих проверок
# 
def calc(op, a, b):
    print(op(a, b))


s = calc(lambda x, y: x+y, 5, 6)
print(s, type(s))

