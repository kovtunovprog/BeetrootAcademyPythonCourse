def oops():
    raise IndexError('Error i raise in purpose')


def catch():
    try:
        oops()
    except IndexError as err:
        print(err)


catch()


def oops2():
    raise KeyError('Error that will pop up')


def catch2():
    try:
        oops2()
    except IndexError:
        print('Error caught!')


catch2()
