def math_operation():
    try:
        a = int(input('Print first number:\n'))
        b = int(input('Print second number:\n'))
        print(a**2 / b)
    except ValueError:
        print("The program only accepts numbers")
        math_operation()
    except ZeroDivisionError:
        print('Second number can\'t be zero!')
        math_operation()


math_operation()

