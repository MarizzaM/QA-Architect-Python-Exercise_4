def add(x=0, y=0):
    return x + y


def sub(x=0, y=0):
    return x - y


def mul(x=0, y=0):
    return x * y


def div(x=0, y=0):
    if y != 0:
        return x / y
    else:
        return 'Error: Div by zero'


n1 = int(input('Please enter first number: '))
n2 = int(input('Please enter second number: '))

print(f'{n1} + {n2} = {add(n1, n2)}')
print(f'{n1} - {n2} = {sub(n1, n2)}')
print(f'{n1} * {n2} = {mul(n1, n2)}')
print(f'{n1} / {n2} = {div(n1, n2)}')
