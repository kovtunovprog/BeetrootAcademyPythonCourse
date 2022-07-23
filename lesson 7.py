users = (
    ('id', 'name', 'balance', 'level', 'kills'),
    ('1', 'Bilbo', '4000', '2', '4'),
    ('2', 'Indigo', '42600', '40', '100'),
    ('3', 'Farmer', '5000', '3', '2'),
    ('4', 'O’rizotto', '5000', '1', '0'),
    ('5', 'Bilbo-1', '0', '1', '0'),
    ('6', 'Bilbo-2', '0', '1', '0'),
    ('7', 'Bilbo-3', '0', '1', '0'),
    ('8', 'O’rizotto-1', '0', '1', '0'),
    ('9', 'O’rizotto-2', '0', '1', '0'),
    ('10', 'O’rizotto-3', '0', '1', '0'),
    ('11', 'O’rizotto-4', '0', '1', '0'),
    ('12', 'Bilbo-1', '4200', '2', '1'),
    ('13', 'GlobalLogic', '720500', '353', '440')
)

def task1():
    '''
    Зробити конвертер данних у дікт
    :return: список словарів
    '''

    next_dict = {}
    dict_keys = users[0]
    result = []

    for i in range(1, len(users)):
        idx = 0
        for key in dict_keys:
            next_dict[key] = users[i][idx]
            idx += 1
        result.append(dict(next_dict))

    return result

def task2():
    '''
    Make a program that has some sentence (a string) on input
    and returns a dictcontaining all unique words as keys and
    the number of occurrences as values.
    :return: none
    '''
    string = input('Enter a sentence: ')
    string = string.replace(",", " ")
    lst = string.split()
    dct = {}

    for i in lst:
        count = lst.count(i)
        dct[i] = count

    print(dct)

def task3():
    '''
    Compute the total price of the stock
    where the total priceis the sum of
    the price of an item multiplied by the quantity
    of this exact item.
    :return:
    '''

    stock = {
        "banana": 6,
        "apple": 0,
        "orange": 32,
        "pear": 15
    }
    prices = {
        "banana": 4,
        "apple": 2,
        "orange": 1.5,
        "pear": 3
    }
    sum = 0
    for fruit in stock.keys():
        sum += stock.get(fruit) * prices.get(fruit)
    print(sum)

def task4():
    '''
    List comprehension exercise
    :return: none
    '''

    base = [i for i in range(1, 11)]
    result = [(i, i**2) for i in base]
    print(result)

def task5():
    '''
    Days of the week
    :return: none
    '''

    lst = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    dct = {}
    dct2 = {}
    idx = 1
    for i in lst:
        dct[idx] = i
        dct2[i] = idx
        idx += 1
    print(dct)
    print(dct2)


if __name__ == '__main__':
    conv = task1()
    for x in conv:
        print(x)
    task2()
    task3()
    task4()
    task5()
