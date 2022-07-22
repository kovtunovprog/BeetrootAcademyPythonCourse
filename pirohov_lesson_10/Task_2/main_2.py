def task2():
    a = int(input('Please enter first number:\n'))
    b = int(input('Please enter second number:\n'))
    return a**2/b


try:
    print(task2())
except ZeroDivisionError:
    print('You can\'t divide by zero!!')
except ValueError:
    print('Please enter valid number(s)!')