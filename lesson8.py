def favourite_movie():
    '''
    Create a simple function called favorite_movie, which takes a string containing
    the name of your favorite movie. The function should then print
    “My favorite movie is named {name}”.
    :return: none
    '''
    name_movie = input('Your favourite movie: ')
    return name_movie

def make_country(name, capital):
    '''
    Creating a dictionary
    param name: Ukraine
    param capital: Kyiv
    return: make_country
    '''

    dct = {name:capital}
    print(f'The capital of {name} is {capital}')
    return dct

def make_operation(operator, *args):
    sum = 0
    mult = 1
    for number in args:
        if operator == '+':
            sum += number
        elif operator == '-':
            sum -= number
        elif operator == '*':
            mult *= number
        else:
            print('Operator is not found')
            return
    if operator == '+':
        print(f'The sum of numbers is {sum}')
    elif operator == '-':
        print(f'The subtraction of numbers is {sum}')
    else:
        print(f'The multiplication of numbers is {mult}')

if __name__ == '__main__':
    name = favourite_movie()
    print(f'My favourite movie is named {name}')
    make_country('Ukraine', 'Kyiv')
    make_operation('-', 3, 7, 8, 9, 4)
    make_operation('+', 6, 7, 8)
    make_operation('*', 8, 8)
    make_operation('/', 9, 3)








