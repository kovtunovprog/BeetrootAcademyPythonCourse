# A simple calculator.

def make_operation(operation, *args):
    math_exp = 0
    if operation == '+':
        for num in args:
            math_exp += num
    elif operation == '-':
        for num in args:
            math_exp -= num
    elif operation == '*':
        math_exp = 1
        for num in args:
            math_exp *= num
    return print(math_exp)



make_operation('*', 7, 6, 2, 2)


