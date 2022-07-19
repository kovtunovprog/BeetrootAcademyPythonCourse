def mult_operation(numbers):

    return_number = 1

    for number in numbers:
        return_number *= number

    return return_number


def make_operation(operation, *numbers):

    numbers = tuple([int(i) for i in numbers if i.isdigit()])

    if operation == "+":
        return sum(numbers)

    if operation == '-':
        return numbers[0] - sum(numbers[1:])

    if operation == '*':
        return mult_operation(numbers)

    else:
        print('Invalid operation')


if __name__ == '__main__':
    user_operation = input('Choose operation(+, -, *):\n')
    user_numbers = input('Print numbers (with space between numbers):\n').split(" ")
    print(make_operation(user_operation, *user_numbers))
