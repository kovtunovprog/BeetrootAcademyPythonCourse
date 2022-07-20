# Task 3

def make_operation(a, *args):
    first_digit = args[0]
    for next_digit in args[1:]:
        if a == '+':
            first_digit += next_digit
        elif a == '-':
            first_digit -= next_digit
        elif a == '*':
            first_digit *= next_digit
        else:
            print('Bad format inserted')
            break
    print(first_digit)

make_operation(input('Please input operation +, - or *: '), 9, 5, 7, 7, 2)