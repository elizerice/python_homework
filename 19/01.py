def arithmetic_operation(operation):
    if operation == '+':
        return lambda x,y: x+y
    elif operation == '-':
        return lambda x,y: x-y
    elif operation == '*':
        return lambda x,y: x*y
    elif operation == '/':
        return lambda x,y: x/y
    else:
        return lambda x,y: print('неверный ввод')


operation = arithmetic_operation('+')
print(operation(1, 4))
